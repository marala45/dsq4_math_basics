# _0101_binomial_distribution.py
# DST_Q3 – Probability
# Topic: Binomial Distribution

import numpy as np
import matplotlib.pyplot as plt
import scipy
from scipy.stats import binom

# Parameters
n = 20           # number of trials
p = 0.5          # probability of success
x = np.arange(0, n+1)  # all possible success counts (0 to 20)

# Binomial probability mass function
pmf = binom.pmf(x, n, p)

# Plot
plt.bar(x, pmf, color='skyblue', edgecolor='black')
plt.title(f'🔢 Binomial Distribution (n={n}, p={p})')
plt.xlabel('Number of Successes')
plt.ylabel('Probability')
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()

