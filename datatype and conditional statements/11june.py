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

"""a=int(input("enter the  number  a: "))
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
"""
task :1 
ask user to enter the number  and  check which  number is  big  small  and  medium. 

input  a=90 
input  b=100
input  c=80
output  : b is  big  a is  medium  c is  small
"""

"""a=int(input("enter the  number  a: "))
b=int(input("enter the  number  b: "))
c=int(input("enter the  number  c: "))

if a >= b and a >= c :  # a= 23 b=  12 c = 1 
    big =a         # big =23 
    if b>=c:        # 12 >=1 
        medium = b     #  medium = 12
        small = c       # small =1 
    else : 
        medium = c  
        small = b   
elif b>=a and b>=c : 
    big =b 
    if a>=c:
        medium = a
        small = c
    else : 
        medium = c
        small = a

elif c>=a  and c >=b :
    big =c
    if a>=b:
        medium = a
        small = b
    else :
        medium = b
        small = a
else : 
    print("same")
    
print("big  is  :",big)
print("medium  is  :",medium)
print("small  is  :",small)
"""

# task :2 
"""
ask user to enter the  character  and check  it is  vowel  consonant  digit or special character.
"""

"""ch =input("enter the  character  : ") #

if ch =='a' or ch =='e'or ch =='i'or ch =='o'or ch =='u': 
    print("it is  vowel")
    
elif ch >'a' and ch <='z' : 
    print("it is  consonant")
    
elif ch >'0' and ch <='9' : 
    print("it is  digit")

else : 
    print("it is  special character")
"""

"""
task :3 ask user to enter the  number and check it is  divisible  by 5 or 11 or both. 

task :4 ask user to  enter the cost  and selling price find out  the  profit and  loss amt .  

task :5 ask user to enter the  3 subjects marks  phy che and maths calculate the  percentage   and give  grade . 

percentage    grade 
90+           A+ 
80-90         A 
70-80         B+
60-70         B
50-60         C+
40-50         C
below 40      Fail 

"""
# loop  : 
"""
1. for    : entry  control  loop    
2. while  : entry  + exit  control  loop

"""

