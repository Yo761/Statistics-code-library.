
import numpy as np

def calculate_range(data):
    return np.max(data) - np.min(data)

data = np.array([10, 20, 30, 40, 50])

result = calculate_range(data)
print("Range:", result)  # 40
