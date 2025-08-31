# _0087_vector_angle.py
# DST_03 – Mathematics for Data Science
# Topic: Vectors – Calculating Angle Between Two Vectors

import numpy as np
import math

# Define two vectors
A = np.array([3, 4, 0])
B = np.array([4, 0, 0])

print("📦 Vector A:", A)
print("📦 Vector B:", B)

# Calculate dot product
dot_product = np.dot(A, B)

# Calculate magnitudes
mag_A = np.linalg.norm(A)
mag_B = np.linalg.norm(B)

# Compute cosine of angle
cos_theta = dot_product / (mag_A * mag_B)

# Compute angle in radians then convert to degrees
theta_rad = math.acos(cos_theta)
theta_deg = math.degrees(theta_rad)

print("🎯 Dot Product:", dot_product)
print("📏 |A| =", round(mag_A, 2), "|B| =", round(mag_B, 2))
print("🧠 cos(θ) =", round(cos_theta, 2))
print("📐 Angle between A and B: {:.2f}°".format(theta_deg))
