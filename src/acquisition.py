"""Acquisition layer: image loading & user interaction.

Contains functions that interact with the user (input/print) to load
the main puzzle image and an individual piece image. These functions
loop until a valid image is loaded and always return a PIL Image.
"""

import os
from PIL import Image


def _select_image_from_directory(directory_path: str, label: str) -> Image.Image:
	"""List images in a directory and let user choose one by index.

	Returns a loaded PIL Image or raises an exception if selection fails.
	"""
	images_iter = os.scandir(directory_path)
	images_list: list[str] = []
	print(f"\nWhich {label} image do you want to select?")
	for idx, entry in enumerate(images_iter):
		if entry.is_file():
			print(f"{idx}. {entry.name}")
			images_list.append(entry.name)

	if not images_list:
		raise FileNotFoundError("No images found in directory.")

	while True:
		try:
			choice = int(input("\nImage number: "))
			if 0 <= choice < len(images_list):
				path = os.path.join(directory_path, images_list[choice])
				return Image.open(path)
			print("❌ Number out of range!")
		except ValueError:
			print("❌ Please enter a valid number!")


def load_puzzle() -> Image.Image:
	"""Interactively load the main puzzle image (loops until success)."""
	default_puzzle_path = r"C:\Users\tiago\Desktop\puzzle_solver\images\puzzles"

	while True:
		print("\n" + "=" * 40)
		print("🧩 Load Puzzle Image! 🧩")
		print("=" * 40)
		print("📸 Use default path (/images/puzzles) or new path?")

		path_choose = input("\n1. Default path \n2. New path\n")

		if path_choose == "1":
			try:
				image = _select_image_from_directory(default_puzzle_path, "puzzle")
				print(f"✅ Puzzle loaded successfully! Size: {image.size[0]} x {image.size[1]} Format: {image.format}")
				return image
			except Exception as e:
				print(f"❌ {e} Try another option.")
				continue
		elif path_choose == "2":
			puzzle_path = input("\nNew puzzle path: ")
			if not os.path.exists(puzzle_path):
				print(f"❌ File {puzzle_path} does not exist! Try again.")
				continue
			try:
				image = Image.open(puzzle_path)
				print(f"✅ Puzzle loaded successfully! Size: {image.size[0]} x {image.size[1]} Format: {image.format}")
				return image
			except Exception as e:
				print(f"❌ Error loading puzzle: {e}")
				continue
		else:
			print("❌ Please choose 1 or 2!")


def load_piece() -> Image.Image:
	"""Interactively load a puzzle piece image (loops until success)."""
	default_piece_path = r"C:\Users\tiago\Desktop\puzzle_solver\images\pieces"

	while True:
		print("\n" + "=" * 40)
		print("🧩 Load Piece Image! 🧩")
		print("=" * 40)
		print("📸 Use default path (/images/pieces) or new path?")

		path_choose = input("\n1. Default path \n2. New path\n")

		if path_choose == "1":
			try:
				image = _select_image_from_directory(default_piece_path, "piece")
				print(f"✅ Piece loaded successfully! Size: {image.size[0]} x {image.size[1]} Format: {image.format}")
				return image
			except Exception as e:
				print(f"❌ {e} Try another option.")
				continue
		elif path_choose == "2":
			piece_path = input("\nNew piece path: ")
			if not os.path.exists(piece_path):
				print(f"❌ File {piece_path} does not exist! Try again.")
				continue
			try:
				image = Image.open(piece_path)
				print(f"✅ Piece loaded successfully! Size: {image.size[0]} x {image.size[1]} Format: {image.format}")
				return image
			except Exception as e:
				print(f"❌ Error loading piece: {e}")
				continue
		else:
			print("❌ Please choose 1 or 2!")


__all__ = ["load_puzzle", "load_piece"]

