# Iterators : An iterator in Python is an object that represents a stream of data and returns one element at a time when you pass it to the built-in next() function

# zip  : a built-in utility used to combine multiple iterables (like lists, tuples, or strings) element-wise into a single iterator of tuples

# enumerate :The enumerate() function in Python is a built-in tool that allows you to loop through an iterable (like a list, tuple, or string) while simultaneously keeping track of the index (position) and the value of each item

# ex :1 ierator 
"""fruits= ["apple","banana","kiwi","mango","cherry"]

fruits_iterator =iter(fruits)

print(next(fruits_iterator))
print(next(fruits_iterator))
print(next(fruits_iterator))
print(next(fruits_iterator))
print(next(fruits_iterator))
"""

# ex :2 zip 

"""
name=['Ravi','Rohit','Rahul','Sachin','Vikas']
age=[25,28,22,27,23]
city=['Delhi','Mumbai','Chennai','Hyderabad','Bangalore']

for i,j,k in zip(name,age,city):
    print(i,j,k)

"""
# ex :3 
"""name= ['Ravi','Rohit','Rahul','Sachin','Vikas']
qty =[2,4,7,5,6]
sales_price =[100,200,300,400,500]

for i,j ,k in zip(name,qty,sales_price):
    print(i,j*k)
"""

# ex :4 enumerate
"""name=['Ravi','Rohit','Rahul','Sachin','Vikas']

# with out using enumerate
index =0 
for i in name:
    print(index,i)
    index +=1

# with  using enumerate : 
for  i ,j in  enumerate(name):
    print(i,j)
"""

# ex :5 

"""students=['Ravi','Rohit','Rahul','Sachin','Vikas']

for i in enumerate(students,start=101):
    print(i)
"""

# generator : use of yield
"""
generator is a special type of function that returns an iterator object, allowing you to produce a sequence of values over time instead of computing them all at once and saving them in memory
"""


# with  using generator :
"""def y(name):
    return 10 
    return 20
print(y("Ravi"))
"""

# using  generator  with yield :
"""def y():
    yield 10
    yield 20
    yield 30
    
demo =y()
print(next(demo))
print(next(demo))
print(next(demo))
"""

# ex :6

"""def bank_transaction():
    
    transactions =["deposit :9000","withdraw :1000","check_balance :8000"]
    
    for i in transactions:
        yield i

demo=bank_transaction()
print(next(demo))
print(next(demo))
print(next(demo))

"""
    