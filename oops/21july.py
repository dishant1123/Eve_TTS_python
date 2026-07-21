# oop  :
"""
4 pillar 

1.inheritance
2.polymorphism 
3.encapsulation :
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

"""class student :
    def __init__(self):
        print("default constructor student class created")
        
    def __init__(self):
        print("student 2 default constructor class created")
s=student()
"""

"""
public : accessible  any where 
private : accessible only inside class
protected : accessible only inside class and sub-class (inheritance)
"""

# ex :1 

"""class student :
    name ="ram"  # public class member 
    age=20
    
    def dispaly(self):
        print("name is : ",self.name)
        print("age is : ",self.age)
s=student()
print("name is  :",s.name)
print("age is : ",s.age)
s.dispaly()
s.name="jyot"
s.age=19
s.dispaly()
"""
# ex :2  private : 

"""class student :
    __name ="ram"  # private class member
    __age=20 
    
    def dispaly(self):
        # self.__name="jyot"
        # self.__age=19
        print("name is : ",self.__name)
        print("age is : ",self.__age)
s=student()
# print("name is  :",s.__name)  # not  accessible  outside the class bcz of private
# print("age is : ",s.__age)
s.dispaly()
s.__name="jyot"
s.__age=19   # not  update  outside the class bcz of private
s.dispaly()
    
"""
# ex :3 

"""class student :
    _name ="meghpreet"   # protected class member
    _age=20 
    
class clg(student):
    def display(self):
        print("name is : ",self._name)
        print("age is : ",self._age)
        
c=clg()
c.display()
"""

# inheritance :
"""
1.single inheritance : only one parent class
    ex : class student :
        class clg(student)

2.multiple inheritance :
    ex : 
        class a  
        class b 
        class c(a,b)

3.multi level inheritance
    ex : 
    class a 
    class b(a)
    class c(b)

4.hierarchical inheritance
    ex : 
        class a 
        class b(a)
        class c(a)
    
5.hybrid inheritance : it is  combination of one  or more than inheritance
    ex : 
        class a 
        class b(a)
        class c(b)
        class d(b,c)
    
"""
# ex :1
"""class student :
    def __init__(self):
        self.__name ="ram"  # private 
        self.age =23 
    def display(self):
        print("name is : ",self.__name)

class clg(student):
    def __init__(self):
        # super().__init__()
        student.__init__(self)
        self.c_name="silver oak university"
        
    def display_1(self):
        self.display()
        print("age is  :",self.age)
        print("c_name is : ",self.c_name)

c=clg()
c.display_1()
"""

# ex :2 without using  constructor

"""class student :
    __name ="meghpreet"   # privateclass member
    age=20

    def display(self):
        print("name is : ",self.__name)

class clg(student):
    c_name="silver oak university"
    
    def display_1(self):
        self.display()
        print("age is  :",self.age)
        print("c_name is : ",self.c_name)

c=clg()
c.age=25
c.__name="jyot"
c.display_1()
c.display()
"""

# ex :3 using parameterized constructor

"""class student :
    def __init__(self,name,age):
        self.__name =name
        self.age =age

    def display(self):
        print("name is : ",self.__name)
        
class clg(student):
    def __init__(self,name,age,c_name):
        # super().__init__(name,age)
        student.__init__(self,name,age)
        self.c_name=c_name
        
    def display_1(self):
        self.display()
        print("age is  :",self.age)
        print("c_name is : ",self.c_name)
        
c=clg("silver oak university")
c.display_1()
"""

# ex : 4 multiple inheritance

"""class student :
    def __init__(self):
        self.name="ram"
        
class teacher :
    def __init__(self):
        self.t_name ="prof.vyas"
        
class clg(student,teacher):
    def __init__(self):
        student.__init__(self)
        teacher.__init__(self)
        self.c_name="silver oak university"
    
c=clg()
print("name  of student is  : ",c.name)
print("name  of teacher is  : ",c.t_name)
print("name  of clg is  : ",c.c_name)
"""
# ex :5 multi level inheritance

"""class grandparent :
    def __init__(self):
        self.g_name="kantilal"
        
class parent(grandparent):
    def __init__(self):
        super().__init__()
        self.p_name="dipak"
    
    def display(self):
        print("name of grandparent is : ",self.g_name)
        print("name of parent is : ",self.p_name)

class child(parent):
    def __init__(self):
        grandparent.__init__(self)
        parent.__init__(self)
        self.c_name="meet"
        
    def display2(self):
        print("name of grandparent is : ",self.g_name)
        print("name of parent is : ",self.p_name)
        print("name of child is : ",self.c_name)
        
# p=parent()
# p.display()
c=child()
c.display2()
"""
# encapsulation : 
"""
  Definition: Encapsulation binds variables and methods into a single unit (class) and controls access to them.

Purpose:
Protects data from unauthorized or accidental modification.
Provides controlled access via getter and setter methods.
Enhances maintainability and abstraction by hiding implementation details.

Access Specifiers in Python:
Public: No underscore prefix. Accessible anywhere.
Protected: Single underscore _var. Accessible but intended for internal use.
Private: Double underscore __var. Not directly accessible outside the class

2 method  : 

1.get_method : data print  
2.set_method : update 
"""

# ex :1 

class employess :
    def __init__(self):
        self.name="ram"
        self.__age=20
        self.__salary=90000
        
    def get_name(self):
        return self.name
    
    def get_age(self):
        return self.__age
    
    def get_salary(self):
        return self.__salary
    
    def set_salary(self,new_salary):
        self.__salary=new_salary
        
    
e=employess()
print("name is : ",e.get_name())
print("age is : ",e.get_age())
print("before using set method employess salary is : ",e.get_salary())

print("new salary  set \n")
e.set_salary(120000)
print("after using set method employess salary is : ",e.get_salary())
