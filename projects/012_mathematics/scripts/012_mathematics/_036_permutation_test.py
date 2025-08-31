# _0120_permutation_test.py
# DST_Q3 – Statistics
# Permutation Test: Compare two groups without assumptions 🧪

import numpy as np
import matplotlib.pyplot as plt

# Simulated data: Group A and Group B
np.random.seed(42)
group_A = np.random.normal(70, 5, 30)   # Group A: mean ~70
np.random.seed(99)
group_B = np.random.normal(73, 5, 30)   # Group B: mean ~73

# Step 1: Actual observed difference
obs_diff = abs(np.mean(group_A) - np.mean(group_B))
print(f"📏 Observed difference in means: {obs_diff:.2f}")

# Step 2: Combine both groups into one
combined = np.concatenate([group_A, group_B])

# Step 3: Run permutation test
n_permutations = 1000
diff_distribution = []
for _ in range(n_permutations):
    np.random.shuffle(combined)
    new_A = combined[:len(group_A)]
    new_B = combined[len(group_A):]
    diff = abs(np.mean(new_A) - np.mean(new_B))
    diff_distribution.append(diff)

# Step 4: Calculate p-value
p_value = np.mean(np.array(diff_distribution) >= obs_diff)
print(f"📈 P-value from permutation test: {p_value:.4f}")

# Step 5: Plot the distribution
plt.hist(diff_distribution, bins=40, color='skyblue', edgecolor='black')
plt.axvline(obs_diff, color='red', linestyle='--', label=f'Observed diff = {obs_diff:.2f}')
plt.title('Permutation Test: Distribution of Differences')
plt.xlabel('Difference in Means')
plt.ylabel('Frequency')
plt.legend()
plt.tight_layout()
plt.show()
