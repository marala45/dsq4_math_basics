# _0105_ttest_mean_small_sample.py
# DST_Q3 – Probability & Statistics
# One-Sample T-Test: Is the sample mean significantly different from a known population mean?

import numpy as np
from scipy.stats import ttest_1samp

# Known population mean (e.g., average male height in the city)
mu = 175  # cm

# Sample data (heights of 10 gym-goers)
sample = np.array([180, 182, 177, 179, 181, 180, 178, 183, 176, 174, 173, 178, 179, 172, 176, 175, 177, 170,  176, 180])

# Calculate sample mean
sample_mean = np.mean(sample)

# Perform one-sample t-test
t_stat, p_value = ttest_1samp(sample, mu)

# Output results
print("📊 Sample Mean:", round(sample_mean, 2))
print("📏 Population Mean (μ):", mu)
print("🧪 T-statistic:", round(t_stat, 3))
print("📈 P-value:", round(p_value, 4))

# Interpretation
alpha = 0.005
if p_value < alpha:
    print("❌ Reject H₀: The sample mean is significantly different from the population mean.")
else:
    print("✅ Fail to reject H₀: No significant difference detected.")
