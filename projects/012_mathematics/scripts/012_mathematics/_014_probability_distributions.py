
# _0098_probability_distributions.py
# DST_Q3 – Probability
# All kinds of Probability Distributions
#   1.	Uniform Distribution – equal chance for all outcomes.
#   2.	Bernoulli Distribution – 0 or 1, success or failure.
#   3.	Binomial Distribution – repeated Bernoulli trials.
#   4.	Normal Distribution – the famous bell curve 📈
#   5.	Poisson Distribution – rare events in fixed intervals.


import random
import numpy as np
import matplotlib.pyplot as plt

# 1. Uniform Distribution
print("\n🎲 Uniform Distribution – Fair Dice Rolls")
for _ in range(10):
    print("Roll:", random.randint(1, 6))

# 2. Bernoulli Distribution
print("\n🟢 Bernoulli Distribution – Success/Failure with p=0.5")
for trial in range(10):
    result = np.random.binomial(1, 0.7)
    print(f"Trial {trial+1}: {'✅ Success' if result == 1 else '❌ Failure'}")

# 3. Binomial Distribution
print("\n🎯 Binomial Distribution – 10 coin tosses, p=0.5")
binomial = np.random.binomial(n=10, p=0.5, size=1000)
plt.hist(binomial, bins=range(0, 12), align='left', rwidth=0.8, color='skyblue', edgecolor='black')
plt.title("Binomial Distribution (n=10, p=0.5)")
plt.xlabel("Number of Successes")
plt.ylabel("Frequency")
plt.grid(True)
plt.show()

# 4. Normal Distribution
print("\n🔔 Normal Distribution – Mean=0, Std=1")
normal = np.random.normal(loc=0, scale=1, size=1000)
plt.hist(normal, bins=30, color='lightgreen', edgecolor='black')
plt.title("Normal Distribution (μ=0, σ=1)")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.grid(True)
plt.show()

# 5. Poisson Distribution
print("\n📊 Poisson Distribution – λ = 3 (avg 3 events/unit)")
poisson = np.random.poisson(lam=3, size=1000)
plt.hist(poisson, bins=range(0, 12), align='left', rwidth=0.8, color='lightcoral', edgecolor='black')
plt.title("Poisson Distribution (λ=3)")
plt.xlabel("Number of Events")
plt.ylabel("Frequency")
plt.grid(True)
plt.show()