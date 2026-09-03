"""
age    salary  

20      20000
23      25000
25      29000
30      35000
34      48000
38      90000

outlier :  2 method   
1.IQR : inter qualtile range  

        IQR = Q3-Q1  
        upper limit = Q3 +1.5*IQR 
        lower limit = Q1-1.5 *IQR
2. Z-score 


"""
import pandas as pd 
import matplotlib.pyplot as plt

df = pd.DataFrame({
    "age" : [20,23,25,30,34 ,38], 
    "salary" :[20000,25000,29000,35000,48000,90000]
})
print(df)
# plt.boxplot(df["salary"])
# plt.legend(loc="upper right")
# plt.title("Salary")
# plt.show()

Q1 = df['salary'].quantile(0.25)
Q3 = df['salary'].quantile(0.75)

print("Q1 = ",Q1)
print("Q3 = ",Q3)
IQR=Q3-Q1
print("IQR = ",IQR)

upper_limit = Q3 + 1.5*IQR
lower_limit = Q1 - 1.5*IQR
print("upper limit = ",upper_limit)
print("lower limit = ",lower_limit)

outlier = df[(df['salary'] > upper_limit) | (df['salary'] < lower_limit)]
print("outlier = ",outlier)

from scipy.stats import zscore

z_score = zscore(df['salary'])
print("z_score = ",z_score)

outlier =z_score[z_score > 2]
print("outlier = ",outlier)


