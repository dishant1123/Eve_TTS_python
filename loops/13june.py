"""
loop : iteration  ===> repeation 
1. for  
2. while
3. while True   
"""

# for  loop  syntax : 
"""
for (variable) in range(start,stop,step) :
    print()
"""
# ex :1-100 : 

"""
for i in range(100) : 
    print(i,end=" ")
"""

# ex :2 
"""
for i in range(1,100,3) : 
    print(i,end=" ")
"""
# ex :100-1 
"""
for i in range(100,0,-1) : 
    print(i,end=" ")

"""

# user  input  : 

# n=int(input("enter the  number  n : "))

# for x in range(1,n+1) :
#     print(x,end=" ")
    
# for x in range(1,n+1,2) :
#     print(x,end=" ")
    
"""
start =int(input("enter the  start  number : "))
end =int(input("enter the  end  number : "))

for i in range(start,end+1,2):
    print(i,end=" ")
"""

# ask user to enter the  number and sum  of  all natural  numbers . 

"""
n=int(input("enter the  number  n : "))   # 5 
sum =0 
for  i in range(1,n+1) :   # 5 , 6 
    sum =sum +i             # sum =15  
print("sum  of  all natural  numbers  is  :",sum)
"""
# ask user to enter the number and  print  factorial  of that number . 
"""
5 factorial  : 5! =1*2*3*4*5 =120 
"""
"""n=int(input("enter the  number  n : "))   # 5 
evensum =0
oddsum =0  
for  i in range(1,n+1) :   # 5 , 6 
    if i % 2==0 :
        evensum =evensum +i
    else :
        oddsum =oddsum +i
print("sum  of  even  numbers  is  :",evensum)
print("sum  of  odd  numbers  is  :",oddsum)
"""
# break ,continue , pass : 

"""
for i in range(1,10) : 
    if i==5 :
        break
    print(i,end=" ")
"""
"""
for i in range(1,10) : 
    if i==5 :
        continue
    print(i,end=" ")
"""
"""
for i in range(1,10) : 
    if i==5 :
        pass
    print(i,end=" ")
"""

# prime  , armstrong number ,reverse number , palindrome number :

# prime  : 

"""
n=int(input("enter the  number  n : "))  # 3 
count =0   
for i in range(1,n+1) :  # 3,4 
    if n % i ==0 :     # 3 % 3 ==0 
        count +=1      # 2 
if count ==2 :
    print("prime")
"""

# armstrong number :

"""n=int(input("enter the  number  n : "))  # 1634
length = len(str(n))    # "1634"  # 4 
sum =0 
temp =n    
while temp >0 :  # 0 > 0
        r = temp %10   # 1 %10 =1
        sum =sum + pow(r,length)  # sum = 1634
        temp //=10   # 1 //10 ==0
    
if sum == n : 
    print("armstrong number")
"""

# reverse number  : 

"""n=int(input("enter the  number  n : "))  # 123
rev =0 

while n >0 :   # 0 > 0 
    r = n %10      # r=1
    rev = rev *10 +r   # rev = 321
    n = n//10    # n =1 //10 =0
    
print("reverse  number  is  :",rev)
"""

l1 =[1,2,3,4]
for i in l1 : 
    print(i,end=" ")