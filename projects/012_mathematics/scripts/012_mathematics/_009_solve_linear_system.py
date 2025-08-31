# _0093_solve_linear_system.py
# DST_Q3 – Linear Algebra for Data Science
# Lesson: Solving Linear Systems – Ax = b

import numpy as np

# Define matrix A and vector b
A = np.array([[2, 1],
              [1, 3]])

b = np.array([8, 13])

print("🔢 Matrix A:")
print(A)
print("\n🎯 Vector b:")
print(b)

# Solve the system Ax = b
x = np.linalg.solve(A, b)
print("\n🧠 Solution x (solves Ax = b):")
print(x)

# Verify the solution
Ax = A @ x
print("\n✅ A * x =")
print(Ax)

eigenvalues, eigenvectors = np.linalg.eig(A)

print("\n🧮 Eigenvalues:")
print(eigenvalues)

print("\n📐 Eigenvectors (columns):")
print(eigenvectors)