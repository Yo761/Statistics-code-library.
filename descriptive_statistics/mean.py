
Formula: \(\bar{x}=\frac{\sum x_i}{n}\)

import numpy as np

def calculate_mean(data):
    return np.mean(data)

data = np.array([10, 20, 30, 40, 50])

result = calculate_mean(data)
print("Mean:", result)  # 30.0
