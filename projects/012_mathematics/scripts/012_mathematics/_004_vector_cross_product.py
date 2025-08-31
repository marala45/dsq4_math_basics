# _0088_vector_cross_product.py
# Q3 – Mathematics for Data Science
# Topic: Vector Cross Product and Orthogonality

import numpy as np

# Define 3D vectors
A = np.array([1, 2, 3])
B = np.array([4, 5, 6])

print("🧮 Vector A:", A)
print("🧮 Vector B:", B)

# Compute cross product
cross_product = np.cross(A, B)
print("✖️ Cross Product (A × B):", cross_product)

# Dot product of original vectors
dot_product = np.dot(A, B)
print("🎯 Dot Product (A • B):", dot_product)

# Check if result is orthogonal to A and B
orthogonal_to_A = np.dot(cross_product, A) == 0
orthogonal_to_B = np.dot(cross_product, B) == 0

print("📏 Orthogonal to A?", "✅ Yes" if orthogonal_to_A else "❌ No")
print("📏 Orthogonal to B?", "✅ Yes" if orthogonal_to_B else "❌ No")
