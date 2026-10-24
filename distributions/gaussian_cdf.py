
from scipy.stats import norm

def calculate_gaussian_cdf(x, mean, sd):
    if sd <= 0:
        raise ValueError("sd must be positive")

    return norm.cdf(x, loc=mean, scale=sd)

x = 60
mean = 50
sd = 10

result = calculate_gaussian_cdf(x, mean, sd)
print("P(X <= 60):", result)  # Approximately 0.8413
