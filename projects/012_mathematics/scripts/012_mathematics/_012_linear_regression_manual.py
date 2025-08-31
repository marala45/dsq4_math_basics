# _0096_linear_regression_manual.py
# DST_Q3 – Linear Algebra + Regression Foundations
# Build Linear Regression from Scratch using NumPy

import numpy as np
import matplotlib.pyplot as plt

# Step 1: Generate simple data
X = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 6, 8, 10])  # Perfect linear relationship (y = 2x)

# Step 2: Initialize parameters
theta0 = 0  # Intercept
theta1 = 0  # Slope
alpha = 0.01  # Learning rate
epochs = 100

n = len(X)
cost_history = []

# Step 3: Gradient Descent Loop
for epoch in range(epochs):
    y_pred = theta0 + theta1 * X
    error = y_pred - y

    cost = (1/n) * np.sum(error ** 2)
    cost_history.append(cost)

    # Gradient calculation
    d_theta0 = (2/n) * np.sum(error)
    d_theta1 = (2/n) * np.sum(error * X)

    # Update parameters
    theta0 -= alpha * d_theta0
    theta1 -= alpha * d_theta1

# Step 4: Print results
print(f"📈 Final model: y = {theta1:.2f}x + {theta0:.2f}")
print(f"🧮 Final cost: {cost_history[-1]:.4f}")

# Step 5: Plot cost history
plt.plot(range(epochs), cost_history)
plt.title("Cost vs Epochs")
plt.xlabel("Epoch")
plt.ylabel("Cost (MSE)")
plt.grid(True)
plt.show()
