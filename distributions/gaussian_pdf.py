
from scipy.stats import norm

def calculate_gaussian_pdf(x, mean, sd):
    if sd <= 0:
        raise ValueError("sd must be positive")

    return norm.pdf(x, loc=mean, scale=sd)

x = 60
mean = 50
sd = 10

result = calculate_gaussian_pdf(x, mean, sd)
print("PDF value:", result)
