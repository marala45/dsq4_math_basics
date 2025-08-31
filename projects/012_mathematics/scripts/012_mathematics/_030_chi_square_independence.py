# _0114_chi_square_independence.py
# DST_Q3 – Statistics
# Chi-Square Test of Independence: Gender vs. Product Preference

import pandas as pd
from scipy.stats import chi2_contingency

# 🎯 Observed frequency table
data = {
    "Product A": [30, 10],
    "Product B": [20, 20],
    "Product C": [10, 30]
}
observed = pd.DataFrame(data, index=["Male", "Female"])
print("📊 Observed Table:")
print(observed)

# 🧠 Chi-square test
chi2, p, dof, expected = chi2_contingency(observed)

# 🔬 Results
print(f"\n📏 Degrees of Freedom: {dof}")
print("📈 Expected Table (if independent):")
print(pd.DataFrame(expected, index=["Male", "Female"], columns=observed.columns))

print(f"\n🔺 Chi-Square Statistic: {chi2:.2f}")
print(f"📉 P-value: {p:.4f}")

if p < 0.05:
    print("❌ Reject H₀: Gender and product preference are dependent.")
else:
    print("✅ Fail to reject H₀: Gender and product preference appear independent.")
    