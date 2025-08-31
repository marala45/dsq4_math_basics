# _0117_anova_teaching_methods.py
# DST_Q3 – Statistics
# ANOVA: Compare exam scores from 3 teaching methods

import numpy as np
from scipy import stats

# Scores from 3 different teaching methods
group_A = [75, 78, 72, 70, 69, 77, 73]
group_B = [85, 87, 83, 82, 86, 88, 90]
group_C = [65, 66, 70, 68, 67, 64, 66]

# Perform one-way ANOVA
f_statistic, p_value = stats.f_oneway(group_A, group_B, group_C)

print("📚 Group A (Traditional):", group_A)
print("🎬 Group B (Video):", group_B)
print("🗣️ Group C (Discussion):", group_C)

print(f"\n🧪 F-statistic: {f_statistic:.2f}")
print(f"📈 P-value: {p_value:.4f}")

# Interpretation
if p_value < 0.05:
    print("❌ Reject H₀: At least one group has a different mean.")
else:
    print("✅ Fail to reject H₀: No significant difference in group means.")