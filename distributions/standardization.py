
import numpy as np

def standardize_data(data):
    mean = np.mean(data)
    sd = np.std(data)

    if sd == 0:
        raise ValueError("Cannot standardize constant data")

    return (data - mean) / sd

data = np.array([10, 20, 30, 40, 50])

result = standardize_data(data)
print("Standardized values:", result)
