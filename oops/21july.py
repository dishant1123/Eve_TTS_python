# oop  :
"""
4 pillar 

1.inheritance
2.polymorphism 
3.encapsulation 
4.abstraction 

class  : blue of print  object 
object : instance of class 

fruits :   <==== class 
    apple
    banana
    orange  <=== object 
    kiwi

"""

#ex :1 

"""class fruits:  # class name  : fruits 
    print("fruits class")   # intializing class
    
f=fruits()  # object name : f
"""
# ex :2 

"""
class factorial :
    def fact(self,n):  # self : key word  function ,constructor access ===> print  
        fact=1
        for i in range(1,n+1):
            fact=fact*i
            return fact 
f=factorial()
print(f.fact(5))
"""

# ex :3 

"""class bank :
    balance =25000 
    def deposit(self,amt):
        self.balance  +=amt 
        print("deposited successfully")
    
    def withdraw(self,amt):
        if self.balance -amt >=10000 :  # 30000 - 22000 >=10000 
            self.balance -=amt
            print("withdrawed successfully")
        else :
            print("min balance required 10000")
    def display(self):
        print("balance : ",self.balance)

b=bank()
b.deposit(5000)
b.withdraw(20000)
b.display()

"""
# constructor   : automatically called when object is created. 
"""
1.default constructor
2.parameterized constructor
3.non-parameterized constructor
4.overloading constructor
"""
# ex :1 default constructor

"""class student :
    def __init__(self) : # default constructor
        print("default constructor")
        print("name is ram")

s=student()
"""

# ex :2 non-parameterized constructor

"""
class student :
    def __init__(self) : # non-parameterized constructor
        self.name="ram"
        self.age=20
        self.city="mumbai"
        print("non-parameterized constructor")
    def display(self):
        print("name is :",self.name)
        print("age is :",self.age)
        print("city is :",self.city)
s=student()
print(s.name,s.age,s.city)
print("name is :",s.name)
print("age is :",s.age)
print("city is :",s.city)
s.display()
"""

# ex :3 parameterized constructor

"""class student :
    def __init__(self,name,age,city) : # non-parameterized constructor
        self.name=name
        self.age=age
        self.city=city
        print("parameterized constructor")
    def display(self):
        print("name is :",self.name)
        print("age is :",self.age)
        print("city is :",self.city)
s=student("ram",20,"mumbai")
s.name="jyot"
s.display()
"""

# ex :4 overloading constructor

class student :
    def __init__(self):
        print("default constructor student class created")
        
    def __init__(self):
        print("student 2 default constructor class created")
s=student()