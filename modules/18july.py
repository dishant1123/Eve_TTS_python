import   random as r

"""choice = r.choice([1,2,3,4,5,"ram",90])
choices = r.choices([1,2,3,"ram",90],k=2)
print(choices)
"""

# sample : 

"""
sample = r.sample([1,2,3,4,5,"ram",90],k=2)
print(sample)
"""

# rock paper scissor :
"""
cases : 
1. u ==r  c ==r  or u==s c==s  or u==p c==p  ===> tie  ===> draw 
2.  u==r and c==s or  u==p  and c==r  or  u==s  and c==p  ===> user win  ===> user_score +=1 
3. else : compouter win  ===> computer_score +=1
"""
"""def game():
    computer_score=0
    user_score=0

    for i in range(5):
        print("GAME NUMBER  : ",i+1)
        
        print("ROCK,PAPER,SCISSOR")
        choices = ["rock","paper","scissor"]

        users=input("enter your choice : ")
        computers =r.choice(choices)

        if users =="rock" and computers =="rock" or users=="paper" and computers=="paper" or users=="scissor" and computers=="scissor":
            print("tie")
            
        if users =="rock" and computers =="scissor" or users=="paper" and computers=="rock" or users=="scissor" and computers=="paper":
            print("user win")
            user_score +=1
        
        if users =="rock" and computers =="paper" or users=="paper" and computers=="scissor" or users=="scissor" and computers=="rock":
            print("computer win")
            computer_score +=1
    
    print("GAME OVER")
    print("SCORE: \n")
    if user_score >computer_score:
        print("user win and user score  : ",user_score)
    else :
        print("computer win and computer score  : ",computer_score)
    
game()
"""
# hw  number  guessing  game .

import math as m 

"""print(m.factorial(5))
print(m.sqrt(25))
print(m.sin(90))
print(m.fsum([1,2,3,4,5]))
print(m.ceil(5.5))
print(m.floor(5.5))
print(m.e)
print(m.pi)
print(m.pow(2,3))
"""

import statistics as s

"""l1=[11,2,3,4,5]

print(s.mean(l1))
print(s.median(l1))
print(s.mode(l1))
print(s.stdev(l1))
print(s.variance(l1))
"""

import datetime as dt

"""today = dt.datetime.today().strftime("%d-%m-%Y %H:%M:%S")
print(today)

now = dt.datetime.now()
print(now)

a=dt.datetime(2022,7,18,12,30,0)
print(a)
print(a.day)
print(a.month)
print(a.year)
print(a.hour)
print(a.minute)
print(a.second)
"""
import time 

"""c_time =time.ctime()
print(c_time)

asc_time =time.asctime()
print(asc_time)

local_time =time.localtime()
print(local_time)

for i in range(5):
    time.sleep(1)
    print(i)
"""

# create your own module : 

# regex :

import  re 
"""txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)
"""

text = "Call me at DIAL555-1234 or office line 555-5678"

# first_search = re.findall(r"\d{3}", text)
# first_search = re.search(r"\d{3}-\d{4}", text)

# print(first_search)

"""alpha = re.findall(r"[a-zA-Z]+", text)
alpha_numreic = re.findall(r"[\w]+", text)
print(alpha_numreic)
"""

email_pattern = re.compile(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}")

email = email_pattern.findall("email@example123.com")
email = email_pattern.findall("em")


"""if email:
    print("email is valid")
else :
    print("email is invalid")
"""  
# hw 

"""
create  a new module 

1.utils.py
    function  : 1. calculation of  percent 
    function  : 2. calculation of  grade 
    function  : 3. enter the  3 subject marks 
2.main.py
"""
# class object : 

"""class student :
    print("hello")
    print("world")
    
s=student()
"""
class emp :
    def __init__(self):
        print("default constructor called ")
        
e=emp()