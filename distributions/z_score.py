
def calculate_z_score(x, mean, sd):
    if sd <= 0:
        raise ValueError("sd must be positive")

    return (x - mean) / sd

x = 80
mean = 60
sd = 10

result = calculate_z_score(x, mean, sd)
print("Z-score:", result)  # 2.0
