# _0110_covariance_correlation_matrix.py
# DST_Q3 – Statistics
# Covariance and Correlation Matrix: Study, Sleep, Exam Scores 🧠📚💤

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Sample data
data = {
    'study_hours': [2, 4, 6, 8, 10, 3, 5, 7, 9, 11],
    'sleep_hours': [8, 7.5, 7, 6.5, 6, 8.5, 7, 6.5, 6, 5.5],
    'exam_score':  [55, 58, 64, 68, 75, 54, 60, 70, 80, 85]
}

# Create DataFrame
df = pd.DataFrame(data)
print("📊 Data:")
print(df)

# Covariance Matrix
cov_matrix = df.cov()
print("\n🔁 Covariance Matrix:")
print(cov_matrix)

# Correlation Matrix
corr_matrix = df.corr()
print("\n🔗 Correlation Matrix:")
print(corr_matrix)

# Heatmap
plt.figure(figsize=(6, 5))
sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Matrix Heatmap")
plt.tight_layout()
plt.show()
