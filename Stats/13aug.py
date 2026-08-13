import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

"""df = pd.DataFrame({
    "employees_id" : range(1,16),
    "salary" :[
        22000, 24000, 25000, 26000, 27000,
        28000, 29000, 30000, 31000, 32000,
        33000, 35000, 38000, 50000, 15000
    ]
})
print(df)
    
# mean salary : 
print("mean salary : ", df['salary'].mean())

# median salary :
print("median salary : ", df['salary'].median())

# mode salary :
# print("mode salary : ", df['salary'].mode())

# skewness salary :
print("skewness salary : ", df['salary'].skew()) 

# histogram of salary :

plt.hist(df['salary'], bins=5,edgecolor='black', color='blue')
plt.title('Histogram of Salary')
plt.xlabel('Salary')
plt.ylabel('Frequency')
plt.show()

"""

# data = [95, 96, 97, 98, 99, 100, 100, 101, 102, 103, 50, 40, 30] 
# data = [5, 6, 7, 8, 9, 10, 11, 12, 50, 60, 70]
# df =pd.DataFrame(data,columns=['Left_Skewed'])

"""data = [10, 20, 30, 40, 50, 60, 70, 60, 50, 40, 30, 20, 10]
df =pd.DataFrame(data,columns=['symmetric'])

print("Skewness:", df["symmetric"].skew())
plt.hist(df['symmetric'], bins=5,edgecolor='black', color='blue')
plt.title('Histogram of Salary')
plt.xlabel('Salary')
plt.ylabel('Frequency')
plt.show()
"""

arr =np.array([23,45,67,12,14,67,88])

print("mean :",np.mean(arr))
print("median :",np.median(arr))
print("variance :",np.var(arr))
print("standard deviation :",np.std(arr))