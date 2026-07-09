# file  handling  : txt 
"""
1. read mode   : only file read + exiting file   
2. write mode  : new file create  +  write + exiting  file open ===> overwrite 
3. append mode : new file create  +  write + exiting  file open ===> last  added

function : 
1. fopen / with open : open file 
2. fclose : file close 
3. f.write : write in file
4. f.read : read from file

"""

# write  mode  :

"""
with  open("meghpreet.txt",'w') as f : 
    f.write("my name is meghpreet.\n")
    f.write("my age is 21.\n")
    f.write("my hobby is coding.\n")
    f.write("dream to meet narendra modi.\n")
    
    f.close()

"""

# write  mode in exiting file  : 

"""with  open("meghpreet.txt",'w') as f : 
    f.write("live in ahmedabad.\n")
    f.write("love to play cricket.\n")
    
"""
# read mode  : 

"""with open("meghpreet.txt",'r') as f :
    # content=f.read()
    # content=f.readline()  # read only  first  line  
    content=f.readlines()  # store in to list. 
    
    print(content)
"""

# append mode  :

with open("meghpreet.txt",'a') as f :
    f.write("best friend name  is  priyanka.\n")
    f.write("both are in same  college.\n")
    

# task  : 1 
"""
ask user to enter the string and separate  the  vowel and consonant in separate file .
input  : my name is meghpreet.

output : vowel.txt : 
        consonant.txt :
"""

"""

task :1 Write a function display_oddLines() to display odd number lines from the text file. Consider the following lines for the file  friends.txt.

Friends are crazy, Friends are naughty !
Friends are honest, Friends are  best !
Friends are like keygen, friends are like license key !
We are nothing without friends, Life is not possible without friends !

task :2 Write a Python program to read a text file and do following: 
1. Print no. of words 
2. Print no. statements 
"""
