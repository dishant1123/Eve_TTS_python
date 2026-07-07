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
    

