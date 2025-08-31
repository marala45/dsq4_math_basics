# _0090_matrix_basics_symmetric.py
# DST_Q3 – Linear Algebra for Data Science
# Lesson: Matrix Basics 🧮

import numpy as np

def check_symmetry(matrix, name):
    if np.array_equal(matrix, matrix.T):
        print(f"✅ Matrix {name} is symmetric.")
    else:
        print(f"❌ Matrix {name} is not symmetric.")

A = np.array([[1, 2, 3],
              [2, 5, 6],
              [3, 6, 9]])

B = np.array([[0, 1],
              [2, 0]])

C = np.array([[4, 0, 0],
              [0, 4, 0],
              [0, 0, 4]])

matrices = {
    "A": A,
    "B": B,
    "C": C
}

for name, mat in matrices.items():
    check_symmetry(mat, name)