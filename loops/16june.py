# nested loop : 
# task :1 ask user to enter the  number and  print  prime  number  between  two range. 

"""
start =int(input("enter the  start  number : "))
end = int(input("enter the  end  number : "))

for i in range(start ,end+1) :   # 6 -101
    count =0    # 0 
    for j in range(1, i+1):  # 1 ,7 
        if i % j ==0 :    #  5 % 5 ==0 
            count +=1     # 2 
    if count ==2 :   # 2==2 
        print(i,end=" ")  # 5 

"""

# task : 2 amg in range  

"""start =int(input("enter the  start  number : ")) # 153 
end = int(input("enter the  end  number : "))  # 50000

i=start   # 153 
while i<=end : 
    temp = i
    digit = len(str(temp))   # 3 
    sum =0 
    while temp > 0  :  # 0 > 0 
        r= temp %10  # r =1 % 10 =1 
        sum =sum + pow(r,digit)  # sum = 153
        temp = temp //10    # temp = 1 //10 =0
    if sum == i :
        print(i,end=" ")  # 153
    i+=1 
"""    

# hw : pelindrome number  in range 

# pattern  : 
"""
1.         2.           3.           
* * * * *   *           * * * * *
* * * * *   * *         * * * * 
* * * * *   * * *       * * * 
* * * * *   * * * *     * * 
* * * * *   * * * * *   *
"""
# 1: 
"""
for i in range(1,6):
    for j in range(1,6):
        print("*",end=" ")
    print()
"""
# 2 : 
"""for i in range(1,6):
    for j in range(1,i+1):
        print("*",end=" ")
    print()
""" 
# 3 : 
"""
for i in range(1,6): # 2
    for j in range(5,i-1,-1): # 5 , 1 
        print("*",end=" ")  # * * * * *
    print()                 # * * * *  
"""
# hw  while  loop 
