def central_limit_therom(data,no_of_samples,sample_size):
    result=[]
    for i in range(no_of_samples):
        sample=np.random.choice(data,size=sample_size,replace=True)
        result.append(np.mean(sample))
    data=np.array(result)
    return data  

data=np.random.randint(1,1000,1000)
no_of_samples=1000
sample_size=30
data=central_limit_therom(data,no_of_samples,sample_size)

import seaborn as sns
sns.distplot(data)
