# _0113_confidence_interval_mean.py
# DST_Q3 – Statistics
# Confidence Interval for a sample mean (95%)

import numpy as np
from scipy import stats

# Simulated sample data (100 exam scores)
np.random.seed(42)
scores = np.random.normal(loc=75, scale=10, size=100)  # mean=75, std=10

# Sample statistics
sample_mean = np.mean(scores)
sample_std = np.std(scores, ddof=1)
n = len(scores)

# Confidence interval (95%)
confidence_level = 0.95
z_score = stats.norm.ppf(1 - (1 - confidence_level) / 2)  # ~1.96
margin_of_error = z_score * (sample_std / np.sqrt(n))
lower_bound = sample_mean - margin_of_error
upper_bound = sample_mean + margin_of_error

# Results
print(f"\U0001F4CA Sample Mean: {sample_mean:.2f}")
print(f"\U0001F4CF Margin of Error: ±{margin_of_error:.2f}")
print(f"✅ 95% Confidence Interval: ({lower_bound:.2f}, {upper_bound:.2f})")
