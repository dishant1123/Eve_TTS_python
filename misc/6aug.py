# exceptional handling :
"""
syntax : 

try 
except 
finally 
"""

# ex :1 zero division error
"""try :
    a=int(input("enter the  value  : "))
    b=int(input("enter the  value  : "))
    result =a/b
    print("result  is  : ",result)
except ZeroDivisionError :
    print("error  :  division by zero")

"""

# ex :2 index out of range error
"""
try :
    l1=[10,20,30,40,50]
    print(l1[2])
except IndexError :
    print("error  :  index out of range")
"""

# ex :3 file not found error
"""try :
    with  open("file.txt",'r') as file:
        context =file.read()
        print(context)
except FileNotFoundError :
    print("file not found plz check the path")
finally :
    print("finally  block file reading successfully")
"""

# ex :4 syntax error

"""
code ='if a>b print("a is greater than b")'
try :
    exec(code)
except SyntaxError :
    print("missed  :  if  a>b colon")
    
finally :
    print("finally  block syntax error successfully")
"""
import csv  as cv 

# read :
"""with open("misc/comments.csv",'r') as file:
    reader =cv.reader(file)
    for  i in reader:
        print(i)   # list 

    dictreader =cv.DictReader(file)
    for  y in dictreader:
        print(y)  # dict 
        
"""
# write :

"""
with open("misc/comments.csv",'a',newline='') as file:
    writer =cv.writer(file)

    writer.writerow(['userId','id','title','body'])
    writer.writerow(["101",'12',"spider man-Brand New Day","sspppyyyydddeeerrrr"])
    
    file.close()
"""

# create the JSON file :

import json

"""with open("misc/students.json",'w') as file:
    data=[
    {
        "name":"priyanka",
        "age":25,
        "address":"ahmedabad",
        "marks":{
            "maths":90,
            "science":80,
            "english":70
        }
    },
    {
        "name":"ramesh",
        "age":25,
        "address":"ahmedabad",
        "marks":{
            "maths":90,
            "science":80,
            "english":70
        }
        
    }]
    file.write(json.dumps(data,indent=4))
    file.close()
    
"""

# read the JSON file :

"""with open("misc/students.json",'r') as file:
    data =json.load(file)
    print(data)
"""   
# using path lib module :

import pathlib
"""
data =pathlib.Path("misc/students.json").read_text()
print(data)

"""

# using os lib module :

import os

