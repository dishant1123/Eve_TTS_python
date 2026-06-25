#string method : 

s1="my name is priyanka."

"""print(s1.capitalize())  # only first letter is capital
print(s1.lower())       # all letters are small
print(s1.upper())       # all letters are capital
print(s1.title())       # first letter is capital and rest are small
print(s1.swapcase())
"""
# count ,index ,rindex ,find , rfind : 
"""print(s1.count("p"))
print(s1.count("a"))
print(s1.count("a",10,20))

print(s1.index("a"))
print(s1.index("a",5,20))
print(s1.index("a",16,20))

print(s1.find("a"))
print(s1.find("a",5,20))
print(s1.find("a",16,20))

# hw difference  between find  , rfind and  index rindex . 

print(s1.rindex("a"))
print(s1.rindex("i"))
print(s1.rindex("i",2,12))

print(s1.rfind("a"))
print(s1.rfind("i"))
print(s1.rfind("i",2,12))
"""

# task  :1  print  all 'o' index number in the string
"""
input : i am going to goa next month. 
output  : first 'o' index number is 6
          second 'o' index number is 12
          third 'o' index number is 14
          fourth 'o' index number is 29

"""

# split , partition , rsplit , rpartition :

s1="my name is priyanka."

"""print(s1.split())
print(s1.split('a'))
print(s1.rsplit('a'))

print(s1.partition('a'))  # divide the string into 3 parts
print(s1.partition(' '))  # divide the string into 3 parts
print(s1.rpartition('a'))  
"""

# replace  :

s1="my name is priyanka and  priyanka is my name."

print(s1.replace("priyanka","ram"))
print(s1.replace("priyanka"," "))
print(s1.replace("priyanka"," ram",2))

"""
task : 2 replace second 'r' with  '#'
input  : restart
output  :resta#t

task :3 ask user to enter the string and replace first space and  last space with underscore.(_)

input : i am going to goa next month.
output : i_am goint to goa next_month.

"""







