# _0086_vector_drill.py
# DST_03 – Mathematics for Data Science
# Linear Algebra: Vector Drill – Practice Basic Operations

import numpy as np

# Define 3 vectors
a = np.array([5, -2, 3])
b = np.array([-1, 4, 2])
c = np.array([0, 0, 1])

print("🚀 Vector A:", a)
print("🚀 Vector B:", b)
print("🚀 Vector C:", c)

# Vector operations
print("➕ A + B:", a + b)
print("➖ B - C:", b - c)
print("✖️ 2 * C:", 2 * c)
print("🎯 Dot(A, B):", np.dot(a, b))
print("📏 Magnitude of B:", round(np.linalg.norm(b), 2))

# Bonus: check if A and C are orthogonal (dot product = 0)
dot_ac = np.dot(a, c)
print("🤖 Are A and C orthogonal?", "Yes" if dot_ac == 0 else "No")