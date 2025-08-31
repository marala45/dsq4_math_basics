# _0085_vector_basics.py
# DST_03 – Mathematics for Data Science
# Lesson: Vector Basics 🧭
# Description:
# This program introduces basic vector operations using NumPy.
# Concepts covered:
# - Creating vectors
# - Vector addition and subtraction
# - Scalar multiplication
# - Dot product
# - Vector magnitude (length)

import numpy as np

# Define two vectors
v1 = np.array([2, 3])
v2 = np.array([1, 4])

# Vector addition
add = v1 + v2

# Vector subtraction
sub = v1 - v2

# Scalar multiplication
scaled = 3 * v1

# Dot product
dot_product = np.dot(v1, v2)

# Magnitude (length) of vector v1
magnitude_v1 = np.linalg.norm(v1)

# Print results
print("🔢 Vector 1:", v1)
print("🔢 Vector 2:", v2)
print("➕ Addition:", add)
print("➖ Subtraction:", sub)
print("✖️ Scaled (3 * v1):", scaled)
print("🎯 Dot Product:", dot_product)
print("📏 Magnitude of v1:", round(magnitude_v1, 2))
