
# _0091_matrix_multiplication_inverse.py
# DST_Q3 – Linear Algebra for Data Science
# Lesson: Matrix Multiplication & Inverse 🧮

import numpy as np

# Define a matrix
A = np.array([[2, 1],
              [5, 3]])

print("🔢 Matrix A:")
print(A)

# Identity matrix
I = np.eye(2)
print("\n🆔 Identity Matrix:")
print(I)

# Multiply A by I
result = A @ I
print("\n✅ A * I =")
print(result)

# Inverse of A
A_inv = np.linalg.inv(A)
print("\n🔁 Inverse of A:")
print(A_inv)

# Validate: A * A_inv = I
validation = A @ A_inv
print("\n🧪 A * A⁻¹ =")
print(validation)

# Round the result for better readability
print("\n🧽 Rounded result (should be close to identity):")
print(np.round(validation, 2))
