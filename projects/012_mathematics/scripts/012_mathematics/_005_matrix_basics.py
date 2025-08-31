# _0089_matrix_basics.py
# DST_Q3 – Linear Algebra for Data Science
# Lesson: Matrix Basics 🧮

import numpy as np

# Define two 2x2 matrices
A = np.array([[2, 4],
              [3, 1]])
B = np.array([[1, 0],
              [5, 2]])

print("🔢 Matrix A:")
print(A)
print("🔢 Matrix B:")
print(B)

# Matrix addition
print("\n➕ A + B:")
print(A + B)

# Matrix subtraction
print("\n➖ A - B:")
print(A - B)

# Scalar multiplication
print("\n✖️ 2 * A:")
print(2 * A)

# Matrix multiplication (dot product)
print("\n🧠 A dot B:")
print(np.dot(A, B))

# Transpose of A
print("\n🔁 Transpose of A:")
print(A.T)

# Identity matrix (2x2)
I = np.identity(2)
print("\n🆔 Identity Matrix:")
print(I)

# Check if A * I = A
print("\n✅ A * I:")
print(np.dot(A, I))
