# escape sequence character : 
"""
1. \n : new line   
2. \t : tab 
3. \b : backspace
4. end =  end of  line     remove  white space . 
"""

"""print("my name is ram.")
print("live in india.")
"""
# example  of  end = : 

"""print("jyot",end="\t\t")
print("pandya")   # jyot pandya
"""

# variable  rules in  python  : 
"""
1. variable  name  can  contain  alphabets  ,  numbers  and  underscores  (_)
2. not space  at  beginning . 
3. exception  : you can use  underscore (_) in between  alphabets .

limitation  : 
1. variable  name  cann't start with  digit ,  special  character (@#$%^&*)
"""
# a12 = 90  # a variable name  90  static  value
# print(a12) 
# print("a12 value is  :",a12) 

# data type  : 
"""
1. int  : pos  or  neg value 
2. float : decimal  value  
3. char / string  : a to z ,  A to Z ,  numbers ,  special  character
4. boolean : True  or  False
5. complex number  : 2  part   1. immginary part  2. real part 
"""

# example  : 

"""a =90000 
print(a)
print("a value is  : ",a)
print(type(a))

b= 945674567560.6888345678456756789 
print(b)
print("b value is  : ",b)
print(type(b))

c='rsefgh'
print(c)
print("c value is  : ",c)
print(type(c))

d= True
print(d)
print("d value is  : ",d)
print(type(d))

e= 34+78j   # 34 real number  78 immginary number
print(e)
print("e value is  : ",e)
print(type(e))

g =90 + 10j 
print(e+g)
"""

# user input  number (int  or  float) : 

"""a =int(input("enter the  a value  : "))
b =int(input("enter the  a value  : "))
print("sum of  two number is  : ",a+b)
"""

# float  : 
"""a =float(input("enter the  a value  : "))
b=float(input("enter the  b value  : "))
print(a)
print(b)
print("sum of  two number is  : ",a+b)
"""

# string  : 

"""a= input("enter the  name  : ")
b=str(input("enter the  surname : "))
print(a)
print(b)
print(a+b)
"""

# type  casting  and  conversion : int  to float 

"""sales=90000
print("total sales  is  : ",sales)
print(type(sales))

print("after  conversion  to  float  sales value  : \n")
total_sales = float(sales)
print("total sales  is  : ",total_sales)
print(type(total_sales))

pincode ="380013" 
print("my pincode is  : ",pincode)
print(type(pincode))

pincode_int = int(pincode)
print("my pincode  in  int  is  : ",pincode_int)
print(type(pincode_int))
"""

# operator  : 
"""
1. airthematic operator  :  + - * / % // 
2. relational operator  :  ==  !=  >  <  >=  <=
3. logical operator  :  and  or  not
4. assignment operator  :  =  +=  -=  *=  /=  %=  //=  **=
5. member operator  :  .  in  not in
"""

"""print(10/3)  # division
print(10%3)  # modulas   : gives  remainder
print(10 //3 )  # floor division

a=90 
b=489
print(a>b and a!=b)
print(a>b or a!=b)

l1=[12,34,56]
print(12 in l1)
print(23 not in l1)

"""

"""
task  : 1 ask user to enter the  number and  concate them . 

input a =89 
input b = 90
output  : 8990

task :2 ask user to enter the  two int type   number  apply divison  of two number  and answer  store in to  the  float.

input  a =91
input b = 6    
output  : 15.67777

task :3 ask user to  enter the  two number  and  print sum , sub , mul ,div and modulas.  
"""
