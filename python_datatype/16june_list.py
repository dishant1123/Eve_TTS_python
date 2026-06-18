# list  : mutable  sequence  of  objects/ elements. you can change the list.

"""
l1 =[1,2,3,4,5,78.9,34+7j,True,False,"priyanka"]
print(l1)
print(type(l1))
"""

# accessing list  element through index :
"""
l1= [1,2,34,56,78,90]
print(l1[0])
print(l1[3])

# update  : 
l1[2] ="ram"
print(l1)
"""

# built-in  function  : len min max sorted reversed sum 

"""l1= [10,2,34,56,78,90]
print(len(l1))
print(min(l1))
print(max(l1))
print(sorted(l1))  # asc to desc 
print(sorted(l1,reverse=True))  # desc to asc
print(sum(l1))
"""
# slicing  : 

"""
l1= [10,2,34,56,78,90]
print(l1[4])  # 78
print(l1[4:6])  # 4 start  6 indexend
print(l1[1:4]) 
print(l1[-1])  # minus index : r to  l 
print(l1[-4])
print(l1[1:5:2])
print(l1[ : : -1])
"""

# method : 
l1= [10,2,34,56,78,90]

"""
l1.append(90000)
print(l1)
"""
# insert : 
"""
l1.insert(3,800)
print(l1)
"""
# copy : 
"""l2 = l1.copy()
l2.append(2000)
print(l1)
print(l2)

l2=l1 
l2.append(2000)
print(l1)
print(l2)
"""

# pop ,remove  : 

l1= [10,2,34,56,78,90]
"""l1.pop()  # by default  last element remove 
print(l1)
l1.pop(3)  # by index
print(l1)

l1.remove(56)
print(l1)
"""

# extend : 
"""
l1= [10,2,34,56,78,90]
l2=["ramesh","priyanka","ram"]

l1.extend(l2)
print(l1)
"""

# for loop  using list : 

"""l1= [10,2,34,56,78,90]

for i in l1 :
    print(i)
"""

# list  in list :

"""l1=[[1,2,3],[4,5,6],[7,8,9]]
print(l1)
print(l1[0][2])
"""

# tuple : immutable  sequence  of  objects/ elements. you can't change the tuple.

"""
t1 =(1,2,3,4,5,78.9,34+7j,True,False,"priyanka")
print(t1)
print(type(t1))
"""

# not change : 
"""t1 =(1,2,3,4,5,78.9,34+7j,True,False,"priyanka")

t1[2] ="ram"
print(t1)  # immutable 
"""

# built-in  function  : len min max sorted reversed

"""
t1=(1,2,34,56,78,90)
print(len(t1))
print(min(t1))
print(max(t1))
print(sorted(t1))  # asc to desc
print(sorted(t1,reverse=True))  # desc to asc
"""
# method : 
"""
t1=(1,2,34,56,78,90)

print(t1.count(56))
print(t1.index(56))
"""
# tuple in tuple  : 
"""t1=((1,2,34,56,78,90),(56,78,90))
print(t1)
print(t1[1][2])
"""

# list to  tuple  : 

"""
input  : l1 =[12,45,67,89]
output : t1 =(12,45,67,89,"ram")
"""
l1 =[12,45,67,89]
l1.append("ram")

print(tuple(l1))


# list example  : to do list 
# tuple example : RGB color 

# task  :1 
"""
ask user to enter the number  append  in the  list  and  print the  sum of all elements of list.
and also separate the  oddsum and  evensum. 

input  : 5   : 23,56,78,90,13   ===> l1 =[23,56,78,90,13]
output  : sum  of all elements  is  : 150   
        oddsum evensum 
"""
"""num =int(input("enter the number "))    
l1=[] 

for i in range(1, num+1):
    n=int(input("enter the number "))
    l1.append(n)
print(l1)  # [12,13,14,15,16]
print("sum  of all elements  is  :",sum(l1))


odd_sum =0 
even_sum =0

for i in l1 :  # [12,13,14,15,16]
    if i% 2==0 :
        even_sum +=i
    else :
        odd_sum +=i
print("oddsum  is  :",odd_sum)
print("evensum  is  :",even_sum)
"""