# _0094_gradient_descent_intro.py
# DST_Q3 – Linear Algebra for Data Science
# Lesson: Gradient Descent Basics 🧠

import numpy as np
import matplotlib.pyplot as plt

# Simulated training data (x and noisy y)
x = np.array([1, 2, 3, 4, 5])
y = np.array([2.1, 3.9, 6.2, 7.8, 10.1])  # Close to y = 2x

# Initialize parameters (slope m and intercept b)
m = 0.0
b = 0.0

# Learning rate and epochs
lr = 0.001
epochs = 1000

# Cost history tracking
cost_history = []

# Gradient Descent loop
for epoch in range(epochs):
    y_pred = m * x + b
    error = y - y_pred
    cost = (error**2).mean()

    # Compute gradients
    m_grad = -2 * (x * error).mean()
    b_grad = -2 * error.mean()

    # Update parameters
    m -= lr * m_grad
    b -= lr * b_grad

    cost_history.append(cost)

print(f"🧠 Final model: y = {m:.2f}x + {b:.2f}")
print(f"📉 Final cost: {cost_history[-1]:.4f}")

# Plotting cost descent
plt.plot(cost_history)
plt.xlabel("Epoch")
plt.ylabel("Cost")
plt.title("Gradient Descent Convergence")
plt.grid(True)
plt.show()
