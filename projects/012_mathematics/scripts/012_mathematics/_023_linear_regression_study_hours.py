# _0107_linear_regression_study_hours.py
# DST_Q3 – Correlation & Regression
# Simple Linear Regression: Study Hours vs. Test Scores 📚✍️

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# 🎓 Data: Hours studied vs. Test scores
hours_studied = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
test_scores = np.array([52, 55, 61, 66, 70, 73, 77, 82, 88, 93])

# 📉 Linear regression calculation
slope, intercept, r_value, p_value, std_err = stats.linregress(hours_studied, test_scores)

# 🔍 Regression line
line = slope * hours_studied + intercept

# 🖨️ Summary
print(f"📈 Regression Equation: y = {slope:.2f}x + {intercept:.2f}")
print(f"🔗 Correlation Coefficient (r): {r_value:.2f}")
print(f"📊 R-squared: {r_value**2:.2f}")
print(f"📈 P-value: {p_value:.4f}")
print(f"📏 Std Error: {std_err:.2f}")

# 📊 Plot
plt.scatter(hours_studied, test_scores, color='blue', label='Data points')
plt.plot(hours_studied, line, color='red', label='Regression line')
plt.title('Study Hours vs. Test Scores')
plt.xlabel('Hours Studied')
plt.ylabel('Test Score')
plt.legend()
plt.grid(True)
plt.show()