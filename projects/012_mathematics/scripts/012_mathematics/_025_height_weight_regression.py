# _0109_height_weight_regression.py
# DST_Q3 – Linear Regression
# Predicting Weight from Height 📏⚖️

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

# 📊 Simulated dataset: Heights (cm) vs Weights (kg)
heights = np.array([150, 155, 160, 165, 170, 175, 180, 185, 190, 195])
weights = np.array([50, 53, 56, 60, 65, 68, 72, 75, 78, 83])

# 📉 Perform linear regression
slope, intercept, r_value, p_value, std_err = linregress(heights, weights)

# 📈 Regression line
line = slope * heights + intercept

# 🔍 Print summary
print(f"📐 Regression Equation: weight = {slope:.2f} * height + {intercept:.2f}")
print(f"🔗 Correlation Coefficient (r): {r_value:.2f}")
print(f"📊 R-squared: {r_value**2:.2f}")
print(f"📈 P-value: {p_value:.4f}")
print(f"📏 Std Error: {std_err:.2f}")

# 📊 Plot the data and regression line
plt.scatter(heights, weights, color='green', label='Data points')
plt.plot(heights, line, color='red', label='Best-fit line')
plt.xlabel("Height (cm)")
plt.ylabel("Weight (kg)")
plt.title("Height vs Weight Regression")
plt.legend()
plt.grid(True)
plt.show()