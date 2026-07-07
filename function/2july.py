# map ,filter ,reduce ,recusive function  : 

# filter  : 

l1=[1,2,3,4,5,6,7,8]

"""
odd=[] 
even=[]
for i in l1 : 
    if i % 2==0 :
        even.append(i)
    else :
        odd.append(i)
print(odd)
print(even)
"""

"""result=list(filter(lambda x : x % 2 ==0,l1))
result1=list(filter(lambda x : x % 2 ==1,l1))

print("sum of even number :",sum(result))
print("sum of odd number :",sum(result1))
"""
# ex :2 

"""l2={19, 65, 57, 39, 152, 639, 121, 44, 90, 190}

result =tuple(filter(lambda y : y % 13 ==0,l2))
result1 =list(filter(lambda y : y % 19 ==0,l2))

print(result)
print(result1)
"""
"""
hw : 
Write a Python program to find palindromes in a given list of strings using Lambda.

Orginal list of strings:
['php', 'w3r', 'Python', 'abcd', 'Java', 'aaa']
List of palindromes:
['php', 'aaa']
"""

# map :  new list  
"""l1=[1,2,6,7,8]
result =[]
for  i in l1 :
    result.append(i*5)
print(result)

result1 =list(map(lambda y : y *5,l1))
print(result1)
"""
# ex :3 
"""
Write a Python program to square and cube every number in a given list of integers using Lambda.

Original list of integers:
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Square every number of the said list:
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
Cube every number of the said list:
[1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]
"""

"""l1= [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = list(map(lambda x : x **2,l1))
result1 = list(map(lambda x : x **3,l1))

print(result)
print(result1)
"""

# reduce :  cummulative

from functools import reduce

"""
l1=[1,2,3,4,5,6,7,8,9,10]

# result = reduce(lambda x,y : x+y,l1)
result = reduce(lambda x,y : x*y,l1)

print(result)
"""

# recursive  function  : function call itself 

#ex :1 factorial 
"""
5! = n*(n-1)! 
"""

"""def facto(n):
    if n==1:
        return 1
    return n * facto(n-1)

print(facto(6))
"""
# ex :2 sum of n natural number  

"""def sum_natural(n):
    if n==1 :
        return 1
    return n + sum_natural(n-1)
print(sum_natural(10))
"""

# ex :3 fibonacci series using loop  for  or  while  : 

"""n=int(input("enter the number of fibonacci series you want to print : "))

a=0 
b=1 
c=0 
for i in range(n):  # 3, 5
    print(a)  # 0 1 1 2 
    c=a+b    # c = 1+2 =3 
    a=b      #   a=2 
    b=c       #  b=3
"""

# using  recurive  function  :
"""def fibonacci(n):
    if n==0 :
        return 0
    elif n==1:
        return 1
    return  fibonacci(n-1) + fibonacci(n-2)

for i in range(10):
    print(fibonacci(i))
    
"""

"""
2.Ask user to give name and marks of 5 different students. Store them in dictionary.
 Sort the above dictionary in ascending order of Marks.
"""

"""1. Write a Python program to sort a list of tuples using Lambda.

Original list of tuples:
[('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
Sorting the List of Tuples:
[('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]
"""

"""l1= [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]

result = sorted(l1,key=lambda x : x[0])
print(result)

"""

"""2. Write a Python program to sort a list of dictionaries using Lambda.

Original list of dictionaries :
[{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]

Sorting the List of dictionaries :
[{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}]
"""
l1 =[{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]

"""r =sorted(l1,key =lambda x : x['make'])
print(r)
"""


