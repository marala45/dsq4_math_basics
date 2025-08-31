# _0102_normal_distribution.py
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

mu = 0      # mean
sigma = 1  # standard deviation

x = np.linspace(-5, 5, 100)
y = norm.pdf(x, mu, sigma)

plt.plot(x, y, label="Normal Distribution", color='purple')
plt.title("📊 Normal Distribution (μ=0, σ=1)")
plt.xlabel("x")
plt.ylabel("Probability Density")
plt.grid(True)
plt.legend()
plt.show()