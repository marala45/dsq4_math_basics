# _0095_learning_rate_comparison.py
# DST_Q3 – Math for Data Science
# Lesson: Gradient Descent – Learning Rate Comparison 📉

import numpy as np
import matplotlib.pyplot as plt

# Generate sample data
X = np.array([1, 2, 3, 4, 5])
y = np.array([3, 5, 7, 9, 11])  # Linear relation y = 2x + 1

# Add bias term (intercept)
X_b = np.c_[np.ones((len(X), 1)), X]

# Mean Squared Error cost function
def compute_cost(X, y, theta):
    m = len(y)
    predictions = X.dot(theta)
    errors = predictions - y
    cost = (1 / (2 * m)) * np.dot(errors, errors)
    return cost

# Gradient Descent function
def gradient_descent(X, y, learning_rate, epochs):
    m = len(y)
    theta = np.random.randn(2)
    cost_history = []

    for _ in range(epochs):
        gradients = (1 / m) * X.T.dot(X.dot(theta) - y)
        theta -= learning_rate * gradients
        cost = compute_cost(X, y, theta)
        cost_history.append(cost)

    return theta, cost_history

# Try different learning rates
learning_rates = [0.01, 0.1, 0.001]
epochs = 100

plt.figure(figsize=(10, 6))
for lr in learning_rates:
    _, cost_hist = gradient_descent(X_b, y, lr, epochs)
    plt.plot(cost_hist, label=f"lr = {lr}")

plt.title("Gradient Descent: Cost vs. Epochs")
plt.xlabel("Epoch")
plt.ylabel("Cost")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
