
# _0104_coin_fairness_test.py
# DST_Q3 – Probability & Statistics
# Z-test to evaluate if a coin is fair (50% heads)

import numpy as np
from scipy.stats import norm

# Constants
p_null = 0.5  # Fair coin
alpha = 0.02  # 98% confidence

# Simulated results: 100000 coin flips (1=heads, 0=tails)
flips = np.random.binomial(1, 0.50, 100000)  # Change 0.55 to simulate bias
num_heads = np.sum(flips)
n = len(flips)
p_hat = num_heads / n  # Sample proportion

# Standard error
se = np.sqrt(p_null * (1 - p_null) / n)

# Z-score
z = (p_hat - p_null) / se

# P-value (two-tailed)
p_value = 2 * (1 - norm.cdf(abs(z)))

print(f"🪙 Total flips: {n}")
print(f"🙂 Heads count: {num_heads}")
print(f"📊 Observed proportion (p̂): {p_hat:.2f}")
print(f"🧠 Z-score: {z:.2f}")
print(f"📈 P-value: {p_value:.4f}")

if p_value < alpha:
    print("❌ Reject H₀: The coin is likely biased.")
else:
    print("✅ Fail to reject H₀: The coin appears fair.")
