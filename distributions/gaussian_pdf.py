
from scipy.stats import norm

def calculate_gaussian_pdf(x, mean, sd):
    if sd <= 0:
        raise ValueError("sd must be positive")

    return norm.pdf(x, loc=mean, scale=sd)

x = 60
mean = 50
sd = 10

result = calculate_gaussian_pdf(x, mean, sd)
print("PDF value:", result)


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

