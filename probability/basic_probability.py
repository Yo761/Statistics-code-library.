
def calculate_probability(favorable, total):
    if total <= 0:
        raise ValueError("total must be positive")
    if favorable < 0 or favorable > total:
        raise ValueError("invalid number of favorable outcomes")

    return favorable / total

favorable = 3
total = 6

result = calculate_probability(favorable, total)
print("Probability:", result)  # 0.5
