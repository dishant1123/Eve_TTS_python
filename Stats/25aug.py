import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 

import seaborn as sns
df = pd.read_csv("Titanic-Dataset.csv")

print(df.head())

df['Age'] =df['Age'].fillna(df['Age'].mean())
df['Sex'] =df['Sex'].map({'male':1,'female':0})

print(df['Sex'])
# print(df.isnull ().sum())


# corr : 

correlation = df.corr(numeric_only=True)

plt.figure(figsize=(10,10))
sns.heatmap(correlation,annot=True,cmap='YlGnBu')
plt.title('Correlation Matrix')

plt.show()