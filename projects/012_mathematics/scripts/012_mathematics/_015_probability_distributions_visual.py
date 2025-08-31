# _0099_probability_distributions_visual.py
# DST_Q3 – Probability Distributions Visualized 🎲📊

import numpy as np
import matplotlib.pyplot as plt
import random

# ------------------------------
# 📊 Simulation Parameters
repetitions = 100
die_faces = 6
bernoulli_p = 0.7
binomial_n = 10
binomial_p = 0.5
normal_mean = 0
normal_std = 1
poisson_lambda = 3

# ------------------------------
# 📦 Generate Samples

# Uniform: Die rolls
uniform_samples = [random.randint(1, die_faces) for _ in range(repetitions)]

# Bernoulli
bernoulli_samples = np.random.binomial(1, bernoulli_p, size=repetitions)

# Binomial
binomial_samples = np.random.binomial(binomial_n, binomial_p, size=repetitions)

# Normal
normal_samples = np.random.normal(normal_mean, normal_std, size=repetitions)

# Poisson
poisson_samples = np.random.poisson(poisson_lambda, size=repetitions)

# ------------------------------
# 🎨 Plotting All Distributions

fig, axs = plt.subplots(3, 2, figsize=(12, 10))
fig.suptitle("📊 Probability Distributions (100 Samples Each)", fontsize=16)

# Uniform
axs[0, 0].hist(uniform_samples, bins=np.arange(1, die_faces + 2) - 0.5, edgecolor='black')
axs[0, 0].set_title("🎲 Uniform (Die Rolls)")
axs[0, 0].set_xticks(range(1, die_faces + 1))

# Bernoulli
axs[0, 1].hist(bernoulli_samples, bins=[-0.5, 0.5, 1.5], edgecolor='black', rwidth=0.7)
axs[0, 1].set_title("✅❌ Bernoulli (p=0.7)")
axs[0, 1].set_xticks([0, 1])

# Binomial
axs[1, 0].hist(binomial_samples, bins=range(0, binomial_n + 2), edgecolor='black')
axs[1, 0].set_title(f"🧪 Binomial (n={binomial_n}, p={binomial_p})")

# Normal
axs[1, 1].hist(normal_samples, bins=15, edgecolor='black')
axs[1, 1].set_title("🔔 Normal Distribution")

# Poisson
axs[2, 0].hist(poisson_samples, bins=range(0, max(poisson_samples)+2), edgecolor='black')
axs[2, 0].set_title("📈 Poisson (λ=3)")

# Remove last empty subplot
fig.delaxes(axs[2, 1])

plt.tight_layout()
plt.subplots_adjust(top=0.9)
plt.show()