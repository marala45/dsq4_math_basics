# _0121_probability_mastery.py
# DST Q33 – Probability Mastery Program
# This file includes:
# - Simulations
# - Visualizations
# - Conceptual notes (in comments)
# For all major probability distributions covered in Q33

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import bernoulli, binom, norm, poisson, geom, expon, hypergeom

# Uniform Distribution
# ---------------------
# Discrete: All integers from a to b have equal probability.
# Continuous: Any real number between a and b has equal probability.
def simulate_uniform_discrete(a=1, b=6, size=100):
    data = np.random.randint(a, b + 1, size)
    sns.histplot(data, bins=np.arange(a, b + 2) - 0.5, kde=False)
    plt.title(f'Discrete Uniform Distribution (a={a}, b={b})')
    plt.xlabel('Outcome')
    plt.ylabel('Frequency')
    plt.show()

# Bernoulli Distribution
# ----------------------
# A single trial with two outcomes: success (1) or failure (0)
def simulate_bernoulli(p=0.3, size=10000):
    data = bernoulli.rvs(p, size=size)
    sns.histplot(data, bins=[-0.5, 0.5, 1.5], kde=False)
    plt.title(f'Bernoulli Distribution (p={p})')
    plt.xlabel('Outcome')
    plt.ylabel('Frequency')
    plt.show()

# Binomial Distribution
# ---------------------
# Repeated Bernoulli trials: number of successes in n trials
def simulate_binomial(n=10, p=0.5, size=10000):
    data = binom.rvs(n, p, size=size)
    sns.histplot(data, bins=n+1, kde=False)
    plt.title(f'Binomial Distribution (n={n}, p={p})')
    plt.xlabel('Number of Successes')
    plt.ylabel('Frequency')
    plt.show()

# Normal Distribution
# -------------------
# Bell-shaped curve defined by mean (mu) and std deviation (sigma)
def simulate_normal(mu=0, sigma=1, size=10000):
    data = norm.rvs(loc=mu, scale=sigma, size=size)
    sns.histplot(data, bins=50, kde=True)
    plt.title(f'Normal Distribution (mu={mu}, sigma={sigma})')
    plt.xlabel('Value')
    plt.ylabel('Density')
    plt.show()

# Poisson Distribution
# --------------------
# Number of events in a fixed interval with rate lambda
def simulate_poisson(lam=4, size=10000):
    data = poisson.rvs(mu=lam, size=size)
    sns.histplot(data, bins=np.max(data) - np.min(data) + 1, kde=False)
    plt.title(f'Poisson Distribution (lambda={lam})')
    plt.xlabel('Event Count')
    plt.ylabel('Frequency')
    plt.show()

# Geometric Distribution
# ----------------------
# Number of trials until the first success
def simulate_geometric(p=0.3, size=10000):
    data = geom.rvs(p, size=size)
    sns.histplot(data, bins=np.max(data), kde=False)
    plt.title(f'Geometric Distribution (p={p})')
    plt.xlabel('Trial of First Success')
    plt.ylabel('Frequency')
    plt.show()

# Exponential Distribution
# ------------------------
# Continuous time until the next event (lambda is rate)
def simulate_exponential(lam=1.0, size=10000):
    data = expon.rvs(scale=1/lam, size=size)
    sns.histplot(data, bins=50, kde=True)
    plt.title(f'Exponential Distribution (lambda={lam})')
    plt.xlabel('Time Until Next Event')
    plt.ylabel('Density')
    plt.show()

# Hypergeometric Distribution
# ---------------------------
# Sampling without replacement from finite population
def simulate_hypergeometric(N=50, K=10, n=5, size=10000):
    data = hypergeom.rvs(M=N, n=K, N=n, size=size)
    sns.histplot(data, bins=np.max(data) - np.min(data) + 1, kde=False)
    plt.title(f'Hypergeometric Distribution (N={N}, K={K}, n={n})')
    plt.xlabel('Successes in Sample')
    plt.ylabel('Frequency')
    plt.show()

def main():
    print("=== Probability Distribution Simulator ===")
    print("Select a distribution to simulate:")
    print("1. Uniform (Discrete)")
    print("2. Bernoulli")
    print("3. Binomial")
    print("4. Normal (Gaussian)")
    print("5. Poisson")
    print("6. Geometric")
    print("7. Exponential")
    print("8. Hypergeometric")
    print("0. Exit")

    choice = input("Enter choice (0–8): ")

    if choice == "1":
        simulate_uniform_discrete()
    elif choice == "2":
        simulate_bernoulli()
    elif choice == "3":
        simulate_binomial()
    elif choice == "4":
        simulate_normal()
    elif choice == "5":
        simulate_poisson()
    elif choice == "6":
        simulate_geometric()
    elif choice == "7":
        simulate_exponential()
    elif choice == "8":
        simulate_hypergeometric()
    elif choice == "0":
        print("Goodbye!")
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()


# Updated interactive menu with repeat loop

def main():
    while True:
        print("\n=== Probability Distribution Simulator ===")
        print("Select a distribution to simulate:")
        print("1. Uniform (Discrete)")
        print("2. Bernoulli")
        print("3. Binomial")
        print("4. Normal (Gaussian)")
        print("5. Poisson")
        print("6. Geometric")
        print("7. Exponential")
        print("8. Hypergeometric")
        print("0. Exit")

        choice = input("Enter choice (0–8): ")

        if choice == "1":
            simulate_uniform_discrete()
        elif choice == "2":
            simulate_bernoulli()
        elif choice == "3":
            simulate_binomial()
        elif choice == "4":
            simulate_normal()
        elif choice == "5":
            simulate_poisson()
        elif choice == "6":
            simulate_geometric()
        elif choice == "7":
            simulate_exponential()
        elif choice == "8":
            simulate_hypergeometric()
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 0 to 8.")

if __name__ == "__main__":
    main()
