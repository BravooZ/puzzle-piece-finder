#!/usr/bin/env python3
"""
Teste de escalas para debugging do matching
"""

def test_scales():
    from src.matching import estimate_piece_scale_factors
    from PIL import Image
    import numpy as np
    
    # Criar imagens de teste
    puzzle = Image.fromarray(np.random.randint(0, 255, (800, 600, 3), dtype=np.uint8))
    piece = Image.fromarray(np.random.randint(0, 255, (100, 100, 3), dtype=np.uint8))
    
    print(f"🧩 Puzzle: {puzzle.size}")
    print(f"🧩 Peça: {piece.size}")
    
    # Testar com número de peças
    scales1 = estimate_piece_scale_factors(puzzle, piece, 24)
    print(f"✅ Escalas com num_pieces=24: {scales1}")
    
    # Testar sem número de peças
    scales2 = estimate_piece_scale_factors(puzzle, piece, None)
    print(f"✅ Escalas sem num_pieces: {scales2}")
    
    # Testar com peça grande
    big_piece = Image.fromarray(np.random.randint(0, 255, (400, 300, 3), dtype=np.uint8))
    scales3 = estimate_piece_scale_factors(puzzle, big_piece, None)
    print(f"✅ Escalas para peça grande {big_piece.size}: {scales3}")

if __name__ == "__main__":
    test_scales()
