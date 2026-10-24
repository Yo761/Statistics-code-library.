
from scipy.stats import norm

def calculate_percentile_value(percentile, mean, sd):
    if not 0 < percentile < 1:
        raise ValueError("percentile must be between 0 and 1")
    if sd <= 0:
        raise ValueError("sd must be positive")

    return norm.ppf(percentile, loc=mean, scale=sd)

mean = 100
sd = 15
percentile = 0.95

result = calculate_percentile_value(percentile, mean, sd)
print("95th percentile:", result)
# Approximately 124.67
