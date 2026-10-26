import math
import numpy as np

def Gaussian_CDF(data):
    result = []

    mean = np.mean(data)
    sd = np.std(data)

    for x in data:
        ans = 0.5 * (
            1 + math.erf((x - mean) / (np.sqrt(2) * sd))
        )
        result.append(ans)

    return np.array(result)
