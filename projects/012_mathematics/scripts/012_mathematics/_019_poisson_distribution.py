# _0103_poisson_distribution.py
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import poisson

lambda_rate = 4  # average number of events
x = np.arange(0, 15)
y = poisson.pmf(x, lambda_rate)

plt.bar(x, y, color='green', alpha=0.7)
plt.title("📊 Poisson Distribution (λ=4)")
plt.xlabel("Number of Events")
plt.ylabel("Probability")
plt.grid(True)
plt.show()