
import numpy as np

def calculate_quartiles_iqr(data):
    q1 = np.percentile(data, 25)
    q2 = np.percentile(data, 50)
    q3 = np.percentile(data, 75)
    iqr = q3 - q1

    return q1, q2, q3, iqr

data = np.array([10, 20, 30, 40, 50, 60, 70])

q1, q2, q3, iqr = calculate_quartiles_iqr(data)

print("Q1:", q1)
print("Q2 (median):", q2)
print("Q3:", q3)
print("IQR:", iqr)
