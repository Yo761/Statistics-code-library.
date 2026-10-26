import numpy as np

def Gaussian_PDF(data):
    result = []

    mean = np.mean(data)
    sd = np.std(data)

    for x in data:
        ans = (1 / (sd * np.sqrt(2 * np.pi))) * np.exp(
            -0.5 * ((x - mean) / sd) ** 2
        )
        result.append(ans)

    return np.array(result)


import math
def Gaussian_CDF(data):
    result=[]
    mean=np.mean(data)
    sd=np.std(data)
    for i in data:
        ans=(i-mean)/(np.sqrt(2)*sd) 
        res=0.5*(1+math.erf(ans))
        result.append(res)
    return np.array(result)

data3=np.sort(data2)
cdf_values=Gaussian_CDF(data3)

