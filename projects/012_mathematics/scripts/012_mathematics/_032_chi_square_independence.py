# _0116_chi_square_independence.py
# DST_Q3 – Statistics
# Chi-Square Test of Independence – Gender vs Product Preference 🛍️

import numpy as np
import pandas as pd
from scipy.stats import chi2_contingency

# 📊 Contingency Table: Rows = Gender, Columns = Product Preference
#            Product A | Product B | Product C
# Male         20           15          30
# Female       25           30          20

data = np.array([[20, 15, 30],
                 [25, 30, 20]])

df = pd.DataFrame(data, columns=["Product A", "Product B", "Product C"],
                  index=["Male", "Female"])

print("🧾 Contingency Table:")
print(df)

# 🔍 Chi-Square Test
chi2, p, dof, expected = chi2_contingency(data)

print(f"📈 Chi-square statistic: {chi2:.2f}")
print(f"🎯 Degrees of freedom: {dof}")
print(f"📉 P-value: {p:.4f}")
print("\n🔢 Expected Frequencies (if independent):")
print(pd.DataFrame(expected, columns=df.columns, index=df.index))

# 📌 Decision
if p < 0.05:
    print("❌ Reject H₀: There's a significant relationship between gender and product preference.")
else:
    print("✅ Fail to reject H₀: No significant relationship detected.")
