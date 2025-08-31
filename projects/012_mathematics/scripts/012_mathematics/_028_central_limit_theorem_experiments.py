# DST_Q3 – Central Limit Theorem
# Visualize how sample size affects normality of sample means

import numpy as np
import matplotlib.pyplot as plt

# Original population (non-normal)
population = np.random.exponential(scale=2.0, size=100000)

# Parameters
sample_size = 10  # 👈 Try 5, 10, 30, 100
num_samples = 1000
sample_means = []

for _ in range(num_samples):
    sample = np.random.choice(population, size=sample_size, replace=False)
    sample_means.append(np.mean(sample))

# Plot
plt.figure(figsize=(12, 5))

# Original Population Histogram
plt.subplot(1, 2, 1)
plt.hist(population, bins=50, color='gray', alpha=0.7)
plt.title("Original Population (Exponential)")
plt.xlabel("Value")
plt.ylabel("Frequency")

# Sample Means Histogram
plt.subplot(1, 2, 2)
plt.hist(sample_means, bins=30, color='green', alpha=0.7)
plt.title(f"Means of {num_samples} Samples (n = {sample_size})")
plt.xlabel("Sample Mean")
plt.ylabel("Frequency")

plt.tight_layout()
plt.show()