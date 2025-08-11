from .acquisition import load_puzzle, load_piece
from .matching import compare_images


# Puzzle Solver - Entry Point
    

def main():
    print("=" * 60)
    print("\n🧩 Welcome to the Puzzle Solver! 🧩")
    print("\nThis program will help you find where puzzle pieces fit!")
    print("=" * 60)
    
    puzzle_image = load_puzzle()
    piece_image = load_piece()

    compare_images(puzzle_image, piece_image)

if __name__ == "__main__":
    main()