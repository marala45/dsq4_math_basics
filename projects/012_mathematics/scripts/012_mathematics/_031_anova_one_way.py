# _0115_anova_one_way.py
# DST_Q3 – Statistics
# One-Way ANOVA: Compare Means Across Multiple Groups 📊

from scipy import stats

# 🎓 Simulated test scores for 3 teaching methods
method_A = [85, 90, 88, 75, 95]
method_B = [70, 65, 80, 72, 68]
method_C = [90, 88, 92, 85, 87]

# 🧪 ANOVA test
f_stat, p_value = stats.f_oneway(method_A, method_B, method_C)

# 📈 Results
print(f"📏 F-statistic: {f_stat:.2f}")
print(f"📈 P-value: {p_value:.4f}")

# 🧠 Interpretation
if p_value < 0.05:
    print("❌ Reject H₀: At least one teaching method differs significantly.")
else:
    print("✅ Fail to reject H₀: No significant difference between methods.")
    