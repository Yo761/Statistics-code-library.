
def calculate_bayes(p_b_given_a, p_a, p_b):
    if p_b <= 0:
        raise ValueError("P(B) must be greater than zero")

    return (p_b_given_a * p_a) / p_b

p_b_given_a = 0.9
p_a = 0.1
p_b = 0.2

result = calculate_bayes(p_b_given_a, p_a, p_b)
print("P(A given B):", result)  # 0.45
