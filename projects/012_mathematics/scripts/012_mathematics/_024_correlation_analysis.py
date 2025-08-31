# _0108_correlation_analysis.py
# DST_Q3 – Statistics
# Correlation analysis between two numerical variables

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import pearsonr

# Simulated data: Study hours vs Exam scores
study_hours = np.array([2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
exam_scores = np.array([50, 55, 60, 63, 65, 70, 75, 78, 85, 88])

# Calculate Pearson correlation
corr_coef, p_value = pearsonr(study_hours, exam_scores)

print("📊 Study Hours:", study_hours)
print("📈 Exam Scores:", exam_scores)
print(f"🧠 Pearson Correlation Coefficient: {corr_coef:.2f}")
print(f"📈 P-value: {p_value:.4f}")

# Interpretation
if p_value < 0.05:
    print("✅ Significant correlation between the two variables.")
else:
    print("❌ No significant correlation detected.")

# Plotting
plt.scatter(study_hours, exam_scores, color='teal', label='Data points')
plt.xlabel("Study Hours")
plt.ylabel("Exam Scores")
plt.title("Correlation: Study Hours vs Exam Scores")
plt.grid(True)
plt.legend()
plt.show()