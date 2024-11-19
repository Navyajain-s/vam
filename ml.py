# mean -- average of dataset 
# numpy helps to find mean 
import numpy as np
dataset = [70,90,65,60,80]
mean = np.mean(dataset)
print(mean)

median = np.median(dataset)
print("median",median)

#we cant find mode in this format we downloaded ext,
# mode = np.mode(dataset)
# print("mode",mode)

from scipy import stats
dataset = [70,90,65,60,80,60,60]
mode=stats.mode(dataset)
print("mode",mode)


#standard deviation
st=np.std(dataset)
print("standard deviation",st)\

max= np.max(dataset)
print("maximum",max)

min= np.min(dataset)
print("minimum",min)


variance = np.var(dataset)
print("variance",variance)

#sd is square root of variance 

#data distribution is a technique to arranging data in order
uniformdata =np.random.uniform(1,10,10)
print(uniformdata)

normaldata =np.random.normal(1,10,10)
print(normaldata)