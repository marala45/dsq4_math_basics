# _0106_two_sample_ttest.py
# DST_Q3 – Statistics
# Compare means of two independent groups (Two-sample t-test)

import numpy as np
from scipy.stats import ttest_ind

# Simulated data: heights of Group A (e.g., athletes) vs Group B (e.g., non-athletes)
group_A = np.array([182, 177, 185, 190, 175, 180, 178, 185, 181, 179])
group_B = np.array([170, 165, 172, 169, 171, 168, 174, 166, 173, 167])

# Calculate means
mean_A = np.mean(group_A)
mean_B = np.mean(group_B)

# Perform two-sample (independent) t-test
t_stat, p_value = ttest_ind(group_A, group_B)

print(f"📏 Mean of Group A: {mean_A:.2f} cm")
print(f"📏 Mean of Group B: {mean_B:.2f} cm")
print(f"🧪 T-statistic: {t_stat:.3f}")
print(f"📈 P-value: {p_value:.4f}")

if p_value < 0.05:
    print("❌ Reject H₀: The means are significantly different.")
else:
    print("✅ Fail to reject H₀: No significant difference between means.")