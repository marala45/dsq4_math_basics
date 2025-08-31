# _0119_bootstrap_confidence_interval.py
# DST_Q3 – Statistics
# Estimate confidence interval of the mean using bootstrapping

import numpy as np
import matplotlib.pyplot as plt

# 🎯 Simulated dataset (e.g., test scores)
data = np.random.normal(loc=75, scale=10, size=50)

# 🔁 Bootstrapping
n_iterations = 1000
sample_means = []

for _ in range(n_iterations):
    sample = np.random.choice(data, size=len(data), replace=True)
    sample_mean = np.mean(sample)
    sample_means.append(sample_mean)

# 🧮 Confidence Interval (95%)
lower_bound = np.percentile(sample_means, 2.5)
upper_bound = np.percentile(sample_means, 97.5)

# 🖨️ Results
print(f"Original Sample Mean: {np.mean(data):.2f}")
print(f"Bootstrapped 95% CI: ({lower_bound:.2f}, {upper_bound:.2f})")

# 📊 Plot
plt.hist(sample_means, bins=30, color="skyblue", edgecolor="black")
plt.axvline(lower_bound, color="red", linestyle="--", label=f"2.5% = {lower_bound:.2f}")
plt.axvline(upper_bound, color="green", linestyle="--", label=f"97.5% = {upper_bound:.2f}")
plt.title("Bootstrapped Sampling Distribution of the Mean")
plt.xlabel("Mean Value")
plt.ylabel("Frequency")
plt.legend()
plt.tight_layout()
plt.show()
