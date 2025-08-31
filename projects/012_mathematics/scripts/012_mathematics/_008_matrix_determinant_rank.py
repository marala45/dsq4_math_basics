# _0092_matrix_determinant_rank.py
# DST_Q3 – Linear Algebra for Data Science
# Lesson: Matrix Determinant and Rank 🔍

import numpy as np

# Define a few sample matrices
A = np.array([[1, 2], [3, 4]])
B = np.array([[2, 4], [1, 2]])
C = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])  # Identity
D = np.array([[1, 2, 3], [2, 4, 6], [3, 6, 9]])  # Rank 1

matrices = {"A": A, "B": B, "C": C, "D": D}

for name, mat in matrices.items():
    print(f"🔢 Matrix {name}:\n{mat}")
    det = np.linalg.det(mat)
    rank = np.linalg.matrix_rank(mat)
    print(f"🧮 Determinant of {name}: {det:.2f}")
    print(f"📏 Rank of {name}: {rank}")
    if det == 0:
        print(f"❌ Matrix {name} is NOT invertible (Singular).")
    else:
        print(f"✅ Matrix {name} is invertible.")
    print("-" * 40)
