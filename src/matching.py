"""Image matching & comparison orchestration."""

import numpy as np
from PIL import Image
from .features import (
	get_image_size,
	compute_area,
	dominant_color,
	color_distance,
	estimate_scale,
)


def compute_mean_abs_diff(img_a: Image.Image, img_b: Image.Image) -> float:
	"""Return mean absolute pixel difference (0 identical .. 255 max).

	Images are converted to RGB, resized must already match.
	Use int16 arrays to avoid uint8 wrap-around when subtracting.
	"""
	a = img_a.convert("RGB")
	b = img_b.convert("RGB")
	if a.size != b.size:
		raise ValueError("Images must have same size for diff")
	arr_a = np.asarray(a, dtype=np.int16)
	arr_b = np.asarray(b, dtype=np.int16)
	diff = np.abs(arr_a - arr_b)
	return float(diff.mean())


def compare_images(puzzle_img: Image.Image, piece_img: Image.Image):
	print("=" * 50)
	print("\n📊 IMAGE PROPERTIES COMPARISON:")
	print("-" * 30)

	# Sizes & areas
	puzzle_size = get_image_size(puzzle_img)
	piece_size = get_image_size(piece_img)
	puzzle_area = compute_area(puzzle_size)
	piece_area = compute_area(piece_size)

	print(f"Puzzle size (px): {puzzle_size} -> area {puzzle_area}")
	print(f"Piece  size (px): {piece_size} -> area {piece_area}")
	area_ratio = piece_area / puzzle_area if puzzle_area else 0
	print(f"Piece / Puzzle area ratio: {area_ratio:.4f}")

	# Dominant colors
	dom_puzzle = dominant_color(puzzle_img)
	dom_piece = dominant_color(piece_img)
	dist = color_distance(dom_puzzle, dom_piece)
	print(f"Dominant color puzzle: {dom_puzzle}")
	print(f"Dominant color piece : {dom_piece}")
	print(f"Euclidean color distance: {dist:.2f}")

	# Scale estimation (ask once)
	print("\nEnter real puzzle width in cm (or blank to skip scale computation):")
	real_width_input = input("> ").strip()
	if real_width_input:
		try:
			real_width_cm = float(real_width_input)
			scale = estimate_scale(puzzle_size[0], real_width_cm)
			print(f"Scale: {scale:.2f} px/cm")
			piece_real_w = piece_size[0] / scale
			piece_real_h = piece_size[1] / scale
			print(f"Estimated piece real size: {piece_real_w:.2f}cm x {piece_real_h:.2f}cm")
		except Exception as e:
			print(f"Scale skipped (error: {e})")
	else:
		print("Scale skipped.")

	# --- Naive global pixel diff baseline ---
	print("\n🔍 Naive pixel diff (piece resized to puzzle size)")
	try:
		piece_resized = piece_img.resize(puzzle_img.size, Image.Resampling.LANCZOS)
		mean_diff = compute_mean_abs_diff(puzzle_img, piece_resized)
		similarity = 1.0 - (mean_diff / 255.0)  # 1 = identical, 0 = maximally different
		print(f"Mean absolute diff: {mean_diff:.2f} (0=identical, 255=max)")
		print(f"Similarity (approx): {similarity*100:.2f}%")
	except Exception as e:
		print(f"Pixel diff failed: {e}")

	print("\n(Next optional: sliding window diff to locate best position.)")

	# Ask user if wants sliding window search
	choice = input("\nRun sliding window local match? (y/N): ").strip().lower()
	if choice == "y":
		_run_sliding_window(puzzle_img, piece_img)


# ===== New pure helpers for GUI / programmatic use =====
def basic_metrics(
	puzzle_img: Image.Image,
	piece_img: Image.Image,
	real_width_cm: float | None = None,
	real_height_cm: float | None = None,
) -> dict:
	"""Compute core metrics without any I/O.

	If real dimensions are supplied (>0), compute pixel-per-cm scale for each axis
	and estimate real piece size using both scales.
	"""
	puzzle_size = get_image_size(puzzle_img)
	piece_size = get_image_size(piece_img)
	puzzle_area = compute_area(puzzle_size)
	piece_area = compute_area(piece_size)
	dom_puzzle = dominant_color(puzzle_img)
	dom_piece = dominant_color(piece_img)
	dist = color_distance(dom_puzzle, dom_piece)
	result: dict = {
		"puzzle_size": puzzle_size,
		"piece_size": piece_size,
		"puzzle_area": puzzle_area,
		"piece_area": piece_area,
		"area_ratio": (piece_area / puzzle_area) if puzzle_area else 0.0,
		"dominant_puzzle": dom_puzzle,
		"dominant_piece": dom_piece,
		"color_distance": dist,
	}
	# Scales
	scale_w = scale_h = None
	try:
		if real_width_cm and real_width_cm > 0:
			scale_w = estimate_scale(puzzle_size[0], real_width_cm)
			result["scale_px_per_cm_width"] = scale_w
	except Exception:
		result["scale_width_error"] = True
	try:
		if real_height_cm and real_height_cm > 0:
			scale_h = estimate_scale(puzzle_size[1], real_height_cm)
			result["scale_px_per_cm_height"] = scale_h
	except Exception:
		result["scale_height_error"] = True
	if scale_w and scale_h:
		result["scale_px_per_cm_avg"] = (scale_w + scale_h) / 2
		result["piece_real_size_cm"] = (
			piece_size[0] / scale_w,
			piece_size[1] / scale_h,
		)
	elif scale_w and not scale_h:
		result["piece_real_size_cm"] = (
			piece_size[0] / scale_w,
			piece_size[1] / scale_w,
		)
	elif scale_h and not scale_w:
		result["piece_real_size_cm"] = (
			piece_size[0] / scale_h,
			piece_size[1] / scale_h,
		)
	return result


def sliding_window_search(puzzle_img: Image.Image, piece_img: Image.Image, stride: int = 4, progress_callback=None) -> dict:
	"""Programmatic sliding window search.

	Returns dict with best_pos, best_diff, similarity, positions_evaluated.
	Optional progress_callback(y, total_rows) for GUI updates.
	"""
	PW, PH = piece_img.size
	MW, MH = puzzle_img.size
	if PW > MW or PH > MH:
		return {"error": "piece_larger_than_puzzle"}
	if stride < 1:
		stride = 1

	puzzle_arr = np.asarray(puzzle_img.convert("RGB"), dtype=np.int16)
	piece_arr = np.asarray(piece_img.convert("RGB"), dtype=np.int16)

	best_diff = None
	best_pos = (0, 0)
	search_w = MW - PW + 1
	search_h = MH - PH + 1
	positions = 0

	for y in range(0, search_h, stride):
		if progress_callback:
			try:
				progress_callback(y, search_h)
			except Exception:
				pass
		for x in range(0, search_w, stride):
			region = puzzle_arr[y:y+PH, x:x+PW, :]
			diff = np.abs(region - piece_arr)
			mad = float(diff.mean())
			positions += 1
			if (best_diff is None) or (mad < best_diff):
				best_diff = mad
				best_pos = (x, y)

	if best_diff is None:
		return {"error": "no_positions"}
	return {
		"best_pos": best_pos,
		"best_diff": best_diff,
		"similarity": 1.0 - (best_diff / 255.0),
		"positions_evaluated": positions,
		"stride": stride,
	}


def _run_sliding_window(puzzle_img: Image.Image, piece_img: Image.Image):
	"""Perform a brute-force (with stride) sliding window diff to locate best match.

	Optimizations:
	- Convert to RGB & numpy arrays once
	- Use int16 for safe subtraction
	- Stride > 1 to speed up (user adjustable prompt)
	"""
	print("\n🚀 Sliding window search starting...")
	PW, PH = piece_img.size
	MW, MH = puzzle_img.size
	if PW > MW or PH > MH:
		print("Piece larger than puzzle in at least one dimension. Skipping.")
		return

	# Get stride from user (default 4)
	stride_in = input("Stride (default 4, smaller = slower & more precise): ").strip()
	try:
		stride = int(stride_in) if stride_in else 4
		if stride < 1:
			stride = 1
	except ValueError:
		stride = 4

	puzzle_arr = np.asarray(puzzle_img.convert("RGB"), dtype=np.int16)
	piece_arr = np.asarray(piece_img.convert("RGB"), dtype=np.int16)

	best_diff = None
	best_pos = (0, 0)
	# Precompute piece flattened for potential vectorization (not required now)

	search_w = MW - PW + 1
	search_h = MH - PH + 1
	positions = 0

	for y in range(0, search_h, stride):
		# Simple progress every ~10 rows
		if y % (max(1, 10 * stride)) == 0:
			print(f"  Row {y}/{search_h - 1}")
		for x in range(0, search_w, stride):
			region = puzzle_arr[y:y+PH, x:x+PW, :]
			diff = np.abs(region - piece_arr)
			mad = float(diff.mean())
			positions += 1
			if (best_diff is None) or (mad < best_diff):
				best_diff = mad
				best_pos = (x, y)

	if best_diff is None:
		print("No positions evaluated (unexpected).")
		return

	similarity = 1.0 - (best_diff / 255.0)
	print(f"\nBest match at (x={best_pos[0]}, y={best_pos[1]})")
	print(f"Best mean abs diff: {best_diff:.2f}")
	print(f"Estimated local similarity: {similarity*100:.2f}%")
	print(f"Positions evaluated: {positions} (stride={stride})")

	# Future: return mask / overlay (could move to visualization)



__all__ = [
	"compare_images",
	"compute_mean_abs_diff",
	"basic_metrics",
	"sliding_window_search",
]


# ===== Advanced / optimized matching =====
def estimate_piece_scale_factors(puzzle_img: Image.Image, piece_img: Image.Image, num_pieces: int | None) -> list[float]:
	"""Return candidate scale factors to resize the piece for matching.

	If num_pieces provided (>1), assume roughly equal area pieces:
	  expected_piece_area = puzzle_area / num_pieces
	  Maintain aspect ratio of provided piece image and solve for width/height.
	Generate a small band around the expected scale (±15%).
	If no num_pieces, use generic scales.
	"""
	pw, ph = piece_img.size
	puzzle_w, puzzle_h = puzzle_img.size
	puzzle_area = puzzle_w * puzzle_h
	if num_pieces and num_pieces > 1 and puzzle_area > 0:
		expected_area = puzzle_area / num_pieces
		aspect = pw / ph if ph else 1.0
		# width * height = expected_area; width = aspect * height => aspect*height^2 = expected_area
		# height = sqrt(expected_area / aspect); width = aspect * height
		import math
		est_h = math.sqrt(expected_area / max(aspect, 1e-6))
		est_w = aspect * est_h
		base_scale = est_w / pw if pw else 1.0
		scales = [base_scale * f for f in (0.85, 1.0, 1.15)]
	else:
		# Generic guess set - escala mais ampla para maior flexibilidade
		scales = [0.4, 0.6, 0.8, 1.0, 1.2, 1.5]
	# Filter scales that would exceed puzzle bounds dramatically (> puzzle dimension *1.1)
	valid = []
	for s in scales:
		if s <= 0:
			continue
		new_w = int(pw * s)
		new_h = int(ph * s)
		# Mais permissivo: permitir peças até 90% do tamanho do puzzle
		if new_w <= puzzle_w * 0.9 and new_h <= puzzle_h * 0.9 and new_w > 4 and new_h > 4:
			valid.append(s)
	return valid or [1.0]


def multi_scale_template_match(
	puzzle_img: Image.Image,
	piece_img: Image.Image,
	num_pieces: int | None = None,
	use_downscale: bool = True,
	method: str = "SQDIFF_NORMED",
	use_gpu: bool = False,
) -> dict:
	"""Fast multi-scale template matching using OpenCV.

	Returns dict with best position, scale, score, similarity estimate and method.
	Automatically downsamples large images for speed and refines coordinates.
	"""
	try:
		import cv2  # local import
	except ImportError:
		return {"error": "opencv_not_available"}

	method_map = {
		"SQDIFF": getattr(cv2, "TM_SQDIFF", None),
		"SQDIFF_NORMED": getattr(cv2, "TM_SQDIFF_NORMED", None),
		"CCORR_NORMED": getattr(cv2, "TM_CCOEFF_NORMED", None),  # alternative
	}
	cv2_method = method_map.get(method.upper(), cv2.TM_SQDIFF_NORMED)

	puzzle_rgb = puzzle_img.convert("RGB")
	piece_rgb = piece_img.convert("RGB")

	import numpy as np
	puzzle_arr = np.asarray(puzzle_rgb)
	piece_arr_orig = np.asarray(piece_rgb)

	# Optional coarse downscale if large
	coarse_scale = 1.0
	max_dim = max(puzzle_arr.shape[0], puzzle_arr.shape[1])
	if use_downscale and max_dim > 1600:
		coarse_scale = 1600 / max_dim
		puzzle_arr_coarse = cv2.resize(puzzle_arr, (int(puzzle_arr.shape[1]*coarse_scale), int(puzzle_arr.shape[0]*coarse_scale)), interpolation=cv2.INTER_AREA)
	else:
		puzzle_arr_coarse = puzzle_arr

	# Gray for speed
	puzzle_gray_coarse = cv2.cvtColor(puzzle_arr_coarse, cv2.COLOR_RGB2GRAY)

	# Optional GPU path (grayscale) for coarse matching if requested
	gpu_available = False
	if use_gpu:
		try:
			if hasattr(cv2, 'cuda') and cv2.cuda.getCudaEnabledDeviceCount() > 0:
				gpu_available = True
		except Exception:
			gpu_available = False

	scale_candidates = estimate_piece_scale_factors(puzzle_img, piece_img, num_pieces)
	results = []

	if gpu_available:
		try:
			gpu_puzzle = cv2.cuda_GpuMat()
			gpu_puzzle.upload(puzzle_gray_coarse)
			for s in scale_candidates:
				resized_piece = cv2.resize(piece_arr_orig, (max(1, int(piece_arr_orig.shape[1]*s*coarse_scale)), max(1, int(piece_arr_orig.shape[0]*s*coarse_scale))), interpolation=cv2.INTER_AREA if s*coarse_scale<1 else cv2.INTER_LANCZOS4)
				ph, pw = resized_piece.shape[:2]
				if ph > puzzle_gray_coarse.shape[0] or pw > puzzle_gray_coarse.shape[1]:
					continue
				piece_gray = cv2.cvtColor(resized_piece, cv2.COLOR_RGB2GRAY)
				gpu_piece = cv2.cuda_GpuMat()
				gpu_piece.upload(piece_gray)
				matcher = cv2.cuda.createTemplateMatching(gpu_puzzle.type(), cv2_method)
				gpu_res = matcher.match(gpu_puzzle, gpu_piece)
				res_mat = gpu_res.download()
				min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res_mat)
				if cv2_method in (cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED):
					score = min_val; loc = min_loc
				else:
					score = -max_val; loc = max_loc
				results.append({
					"scale": s,
					"coarse_location": loc,
					"score": score,
					"piece_size_scaled": (pw, ph),
				})
		except Exception:
			gpu_available = False  # fallback to CPU

	if not gpu_available:
		for s in scale_candidates:
			resized_piece = cv2.resize(piece_arr_orig, (max(1, int(piece_arr_orig.shape[1]*s*coarse_scale)), max(1, int(piece_arr_orig.shape[0]*s*coarse_scale))), interpolation=cv2.INTER_AREA if s*coarse_scale<1 else cv2.INTER_LANCZOS4)
			ph, pw = resized_piece.shape[:2]
			if ph > puzzle_gray_coarse.shape[0] or pw > puzzle_gray_coarse.shape[1]:
				continue
			piece_gray = cv2.cvtColor(resized_piece, cv2.COLOR_RGB2GRAY)
			match = cv2.matchTemplate(puzzle_gray_coarse, piece_gray, cv2_method)
			min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(match)
			if cv2_method in (cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED):
				score = min_val; loc = min_loc
			else:
				score = -max_val; loc = max_loc
			results.append({
				"scale": s,
				"coarse_location": loc,
				"score": score,
				"piece_size_scaled": (pw, ph),
			})

	if not results:
		return {"error": "no_valid_scale"}

	# Pick best (lowest score)
	best = min(results, key=lambda r: r["score"])

	# Refine at full resolution around region
	refine_radius = 30  # pixels in coarse space
	(coarse_x, coarse_y) = best["coarse_location"]
	full_x_est = int(coarse_x / coarse_scale)
	full_y_est = int(coarse_y / coarse_scale)

	# Prepare full-res piece at best scale
	best_scale = best["scale"]
	full_piece = cv2.resize(piece_arr_orig, (int(piece_arr_orig.shape[1]*best_scale), int(piece_arr_orig.shape[0]*best_scale)), interpolation=cv2.INTER_LANCZOS4 if best_scale>1 else cv2.INTER_AREA)
	piece_h, piece_w = full_piece.shape[:2]

	# Define search window in full-res
	x0 = max(0, full_x_est - refine_radius)
	y0 = max(0, full_y_est - refine_radius)
	x1 = min(puzzle_arr.shape[1]-piece_w, full_x_est + refine_radius)
	y1 = min(puzzle_arr.shape[0]-piece_h, full_y_est + refine_radius)

	best_ref_score = None
	best_ref_pos = (full_x_est, full_y_est)

	# Use same method for refinement (convert to gray once)
	puzzle_gray_full = cv2.cvtColor(puzzle_arr, cv2.COLOR_RGB2GRAY)
	piece_gray_full = cv2.cvtColor(full_piece, cv2.COLOR_RGB2GRAY)

	for yy in range(y0, max(y0+1, y1+1)):
		for xx in range(x0, max(x0+1, x1+1)):
			patch = puzzle_gray_full[yy:yy+piece_h, xx:xx+piece_w]
			if patch.shape[0] != piece_h or patch.shape[1] != piece_w:
				continue
			# Fast SAD approximation using mean abs diff
			diff = np.abs(patch.astype(np.int16) - piece_gray_full.astype(np.int16))
			mad = float(diff.mean()) / 255.0  # normalize 0..1
			if best_ref_score is None or mad < best_ref_score:
				best_ref_score = mad
				best_ref_pos = (xx, yy)

	# Similarity heuristic
	similarity = 1.0 - (best_ref_score if best_ref_score is not None else 1.0)

	return {
		"best_position": best_ref_pos,
		"scale": best_scale,
		"piece_size_final": (piece_w, piece_h),
		"score": best["score"],
		"refined_similarity": similarity,
		"method": method,
		"coarse_scale_factor": coarse_scale,
		"candidates_considered": len(results),
		"scale_candidates": [r["scale"] for r in results],
		"gpu_used": gpu_available,
	}


__all__.extend([
	"estimate_piece_scale_factors",
	"multi_scale_template_match",
])

