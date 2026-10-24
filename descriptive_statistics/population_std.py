
import numpy as np

def calculate_population_std(data):
    return np.std(data)

data = np.array([10, 20, 30, 40, 50])

result = calculate_population_std(data)
print("Population standard deviation:", result)
# Approximately 14.1421
