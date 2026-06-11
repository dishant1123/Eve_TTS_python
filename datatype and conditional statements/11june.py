# python data types  : 
"""
1.string  : immutable  sequence of  characters  ===> you can't change the string. 
2. list   : mutable  sequence  of  objects  ===> you can change the list.
3. tuple  : immutable  sequence  of  objects  ===> you can't change the tuple.
4. dictionary : mutable  sequence  of  key-value  pair  ===> you can change the dictionary.
5. set      : mutable  sequence  of  unique  objects  ===> you can change the set.
"""

# conditional statements :
"""
if else  : 

if (con) :
    print()
else :
    print()
"""
# ex :1 

"""
age=int(input("enter the  number age : "))

if age >18 :
    print("you are  eligible  for vote")
else :
    print("you are not eligible  for vote")
"""
# nested if  : 
"""
syntax : 
    if con : 
        if(con) :
            print()
        else :
            print()
    elif con :
        if (con) :
            print()
        else :
            print()
"""
# ex :2
"""
a=int(input("enter the  number  a: "))
b=int(input("enter the  number  b: "))
c=int(input("enter the  number  c: "))

if a>b : 
    if a>c :
        print("a is  big")
    else :
        print("c is  big")
elif b>a :
    if b>c :
        print("b is  big")
    else : 
        print("c is  big")
else : 
    print("same")
"""
# ladder if : 
"""
if (con) : 
    print()
elif (con) :
    print()
else :
    print()

"""

# ex :3 

a=int(input("enter the  number  a: "))
b=int(input("enter the  number  b: "))
c=int(input("enter the  number  c: "))

if a>b and a>c : 
    print("a is  big")
elif b>a and b>c :
    print("b is  big")
elif c>a and c>b :
    print("c is  big")
else:
    print("same")
    
"""
task :1 
ask user to enter the number  and  check which  number is  big  small  and  medium. 

input  a=90 
input  b=100
input  c=80
output  : b is  big  a is  medium  c is  small
"""
