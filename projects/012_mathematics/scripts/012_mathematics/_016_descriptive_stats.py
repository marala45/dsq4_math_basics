# _0100_descriptive_stats.py
# DST_Q3 – Probability & Statistics
# Descriptive statistics on 100 student scores

import numpy as np

scores = [78, 91, 68, 54, 82, 47, 60, 78, 97, 58, 62, 50, 50, 63, 92, 75, 79, 63, 42, 61, 92, 41, 63, 83, 69, 77, 41, 99, 60, 72, 51, 97, 61, 83, 64, 88, 66, 98, 81, 67, 99, 55, 54, 86, 90, 83, 94, 91, 96, 42, 76, 90, 46, 60, 48, 78, 57, 43, 64, 99, 53, 89, 97, 48, 65, 92, 41, 59, 67, 86, 99, 46, 83, 47, 86, 74, 53, 56, 75, 89, 79, 43, 41, 45, 93, 81, 43, 93, 68, 57, 65, 83, 73, 49, 75, 53, 70, 87, 54, 47]

mean = np.mean(scores)
median = np.median(scores)
mode = int(np.bincount(scores).argmax())
std_dev = np.std(scores)
variance = np.var(scores)
min_score = np.min(scores)
max_score = np.max(scores)
range_score = max_score - min_score

print("📊 Descriptive Statistics for 100 Student Scores")
print("Mean:", round(mean, 2))
print("Median:", median)
print("Mode:", mode)
print("Standard Deviation:", round(std_dev, 2))
print("Variance:", round(variance, 2))
print("Min Score:", min_score)
print("Max Score:", max_score)
print("Range:", range_score)
