# _0111_bayes_theorem.py
# DST_Q3 – Probability & Statistics
# Reusable Bayes' Theorem function with real-world simulation examples

def bayes_theorem(p_positive_given_disease, p_disease, p_positive_given_healthy):
    p_healthy = 1 - p_disease
    # Total probability of testing positive
    p_positive = (p_positive_given_disease * p_disease) + (p_positive_given_healthy * p_healthy)

    # Bayes' Theorem
    p_disease_given_positive = (p_positive_given_disease * p_disease) / p_positive

    return p_disease_given_positive, p_positive


# 🧪 Example 1: Disease test with low prevalence
p_pos_given_disease = 0.99  # 99% true positive rate
p_disease = 0.01            # 1% of population has the disease
p_pos_given_healthy = 0.05  # 5% false positive rate

posterior, evidence = bayes_theorem(p_pos_given_disease, p_disease, p_pos_given_healthy)

print("🔬 Bayes' Theorem – Diagnostic Test Example")
print(f"📈 P(Disease | Positive): {posterior:.4f} or {posterior*100:.2f}%")
print(f"📊 P(Positive): {evidence:.4f} or {evidence*100:.2f}%")

# 🧪 Try another test with higher prevalence
print("\n🧪 Example 2: Disease prevalence at 20%")
posterior2, evidence2 = bayes_theorem(0.99, 0.2, 0.05)
print(f"📈 P(Disease | Positive): {posterior2:.4f} or {posterior2*100:.2f}%")
print(f"📊 P(Positive): {evidence2:.4f} or {evidence2*100:.2f}%")
