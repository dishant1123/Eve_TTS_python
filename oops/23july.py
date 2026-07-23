# polymorphism : many forms of the same function
"""
2 method : 
1. method overloading  
2. method overriding

"""

# ex :1  method  overloading  :  not required inheritance in method overloading

"""class math : 
    def add(self,a,b):
        return a+b
    
    def add(self,a,b,c):
        return a+b+c 
    
m=math()
print(m.add(23,56,90))    
print(m.add(10,20,30)) 
"""
# ex :2 default pameter : 

"""class math:
    def add(self,a,b,c=90):
        return a+b+c 
    
m=math()
print(m.add(12,45))
print(m.add(1,2,3))

"""

# ex :3 *args

"""class math :
    def add(self,*args):  # args take only num arg 
        return sum(args)
    
m=math()
print(m.add(1,2,3))
print(m.add(1,2,3,3,4,5,6,7))
print(m.add(1))
"""

# method overriding : inheritance  is  required in method overriding. 

"""class animal:
    def eat(self):
        print("animal eat")
        
class bird(animal):
    def eat(self):
        print("bird can also eat")
        
class cat(animal):
    def eat(self):
        print("cat can also eat")
        
# c=cat()
# c.eat()

a=[cat(),bird(),animal()]
for i in a :
    i.eat()
"""

# class method : 
"""
1. cls key word  as first arg. 
2. class method is directly called on class name.
3. can  be modify 
4. declared  class method using  decorator  of  : @classmethod
"""
"""class student :
    
    clg="ABC_clg"
    @classmethod
    def name_of_clg(cls):
        print("clg name is  :",cls.clg)

student.name_of_clg()  # directly access class method  using class name
""" 
# update using  cls :
"""class student :
    
    clg="ABC_clg"
    @classmethod
    def name_of_clg(cls,new_clg):
        cls.clg=new_clg
        print("clg name is  :",cls.clg)

student.name_of_clg("LJ clg")  # directly access class method  using class name
"""
#static method : 
"""
1. declared  static method using  decorator  of  : @staticmethod
2. static method works as same as function.
3. not  modify 
4. not  first arg is  cls 
"""

"""class calculations :
    
    @staticmethod
    def add(a,b):
        print("add is ",a+b)
    
    @staticmethod
    def sub(a,b):
        print("sub is ",a-b)
        
c=calculations()
c.add(10,20)
c.sub(90,67)
"""

# abstraction  : hiding  implementation  details and  only show essential features.
"""
ex : car  ===> break,cluch,accelerate,stearing  ====> 

1. from abc import ABC ===> abstract base class 
2. @abstractmethod 
3. you can't create object of abstract class. 
"""

from abc import ABC,abstractmethod

class Four_wheeler(ABC):
    
    @abstractmethod
    def model(self):
        pass 

    @abstractmethod
    def speed(self):
        pass 
    
class  car(Four_wheeler):
    
    def model(self):
        print("car model : BMW-Q6")
    
    def speed(self):
        print("car speed : 100km/h")

c=car()
c.model()
c.speed()
