
# _0097_manual_linear_regression.py
# DST_Q3 – Linear Algebra + Modeling
# Manual Linear Regression (Closed-Form Solution)

import numpy as np
import matplotlib.pyplot as plt

# New data (clear linear pattern)
x = np.array([1, 2, 3, 4, 5])
y = np.array([2.1, 4.1, 6.0, 7.9, 10.1])

# Calculate slope (b) and intercept (a)
x_mean = np.mean(x)
y_mean = np.mean(y)
b = np.sum((x - x_mean) * (y - y_mean)) / np.sum((x - x_mean) ** 2)
a = y_mean - b * x_mean

# Predict values
y_pred = a + b * x

# Show results
print(f"📊 Best-fit line: y = {b:.2f}x + {a:.2f}")

# Plot
plt.scatter(x, y, label="Data Points")
plt.plot(x, y_pred, color='red', label="Regression Line", linewidth=2)
plt.legend()
plt.title("Manual Linear Regression")
plt.grid(True)
plt.show()
