
import numpy as np

def calculate_sample_variance(data):
    return np.var(data, ddof=1)

data = np.array([10, 20, 30, 40, 50])

result = calculate_sample_variance(data)
print("Sample variance:", result)  # 250.0
