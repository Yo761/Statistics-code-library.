
from scipy.stats import norm

def gaussian_probability_between(a, b, mean, sd):
    if sd <= 0:
        raise ValueError("sd must be positive")
    if a > b:
        raise ValueError("a must be <= b")

    return (
        norm.cdf(b, loc=mean, scale=sd)
        - norm.cdf(a, loc=mean, scale=sd)
    )

mean = 60000
sd = 10000
a = 40000
b = 80000

result = gaussian_probability_between(a, b, mean, sd)
print("Probability:", result)
print("Percentage:", result * 100, "%")
# Approximately 95.45%
