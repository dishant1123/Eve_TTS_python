# local variable  : 

"""
def x():
    y=10    # local variable
    print(y) 
x()
# print(y)   # out  side  you cant access the local variable  . 

"""

# global variable : access any where also  update using  global keyword 

"""
x=100 
def y():
    print("inside the function  access the x value  :",x)
y()
print("outside the  function access  the x value  :",x)
"""

# modify the  global variable  using  global keyword : 

"""
x=100 
def y():
    global x
    x=200 
    print("inside the function  access the updated  x value  :",x)
    
y()
print("outside the  function access  the x value  :",x)
"""
# *args : only take  number arguments . 

"""
def sum1(a,b=90):
    print(a+b)
sum1(10,78)
"""
"""
def sum1(*args):
    return sum(args)
print(sum1(1,23,45,46,78,90,78.89))
"""
# **kwargs : only take  keyword  and value  arguments .

"""def d1(**kwargs):
    for i , j in kwargs.items():
        print(f"{i} : {j}")
d1(ram=90,a=100,pandya=200)
"""

# lambda :  one liner function  
"""
syntax : 

lambda  arguments : expression
"""
# ex:1 
"""def sum1(a,b):
    return a+b
print(sum1(10,78))

result = lambda a,b : a+b
print(result(10,78))
"""

# ex :2 print 

"""a =lambda x : print("my name is  :",x)
a("jyot")
"""

# ex :3 

"""def big (a,b):
    if a>b :
        return a
    else :
        return b
    
print(big(238,56))

result = lambda a,b  :  print("a is  big",a) if a>b else (print("b is big",b))
result(23,56)
"""

# ex :4 ask user to take  3 number and  print  big number . 

"""r =lambda a,b,c : max(a,b,c)
r1 =lambda a,b,c : min(a,b,c)
r2 =lambda a,b,c : sorted([a,b,c])

print(r(230,576,78))
print(r1(230,576,78))
print(r2(230,576,78))
"""

# using data type  : 

"""a=lambda x : len(x)
print(a("jyot"))
print(a([1,2,3,4,5]))
print(a((1,2,3,4,5,6,7,8,9,10)))
print(a({"a":1,"b":2,"c":3}))
print(a({1,2,3,4,4}))

b=lambda *args : sum(args)
print(b(1,2,3,4,5,6,7,8,9,10))
print(b(1,2,3,4,5))
"""
# 