
import numpy as np

def calculate_sample_std(data):
    return np.std(data, ddof=1)

data = np.array([10, 20, 30, 40, 50])

result = calculate_sample_std(data)
print("Sample standard deviation:", result)
# Approximately 15.8114
