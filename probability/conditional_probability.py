
def calculate_conditional_probability(p_intersection, p_b):
    if p_b <= 0:
        raise ValueError("P(B) must be greater than zero")

    return p_intersection / p_b

p_intersection = 0.2
p_b = 0.4

result = calculate_conditional_probability(p_intersection, p_b)
print("P(A given B):", result)  # 0.5
