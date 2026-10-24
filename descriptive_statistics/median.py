
import numpy as np

def calculate_median(data):
    return np.median(data)

data = np.array([10, 20, 30, 40, 50])

result = calculate_median(data)
print("Median:", result)  # 30.0
