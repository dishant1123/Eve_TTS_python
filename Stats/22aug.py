from scipy.stats import ttest_1samp
import numpy as np 

"""
A company normally gets an average productivity of 50 units per day. After introducing a new software tool, the company records productivity for 10 employees.
Sample data:
52, 55, 49, 58, 54, 51, 56, 53, 57, 55



"""

# Productivity data after new software
productivity = np.array([52, 55, 49, 58, 54, 51, 56, 53, 57, 55])

# One-sample t-test against the old average (50 units/day)
t_stat, p_val = ttest_1samp(productivity, 50)

print("mean:", productivity.mean())
print("sample size:", len(productivity))   # 10 
print("standard deviation:", productivity.std())
print("variance:", productivity.var())

print("t-statistic:", t_stat)
print("p-value:", p_val)

if p_val < 0.05:
    print("Reject H0")
    print("There is significant evidence that productivity changed.")
    
else :
    print("Fail to reject H0")
    print("There is not enough evidence that productivity changed.")

