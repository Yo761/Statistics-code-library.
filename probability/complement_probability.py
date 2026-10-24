
def calculate_complement(probability):
    if not 0 <= probability <= 1:
        raise ValueError("probability must be between 0 and 1")

    return 1 - probability

probability = 0.7

result = calculate_complement(probability)
print("Probability of not A:", result)  # 0.3
