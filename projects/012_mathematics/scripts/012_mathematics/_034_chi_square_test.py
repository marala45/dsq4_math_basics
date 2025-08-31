# _0118_chi_square_test.py
# DST_Q3 – Statistics
# Chi-Square Test of Independence: Categorical Association Analysis

import numpy as np
import pandas as pd
from scipy.stats import chi2_contingency

# 📊 Observed data (Contingency Table)
data = {
    "Likes Cats":   [20, 35],  # [Men, Women]
    "Likes Dogs":   [30, 15]
}

index = ["Men", "Women"]
df = pd.DataFrame(data, index=index)
print("\n📋 Observed Data:")
print(df)

# 🧪 Chi-Square Test
chi2, p, dof, expected = chi2_contingency(df)

print("\n🔢 Expected Frequencies:")
print(pd.DataFrame(expected, index=index, columns=df.columns))

print(f"\n🧮 Chi-Square Statistic: {chi2:.2f}")
print(f"📈 Degrees of Freedom: {dof}")
print(f"📉 P-value: {p:.4f}")

# ✅ Interpretation
alpha = 0.05
if p < alpha:
    print("\n❌ Reject H₀: There IS a significant relationship between gender and pet preference.")
else:
    print("\n✅ Fail to reject H₀: There is NO significant relationship between gender and pet preference.")
