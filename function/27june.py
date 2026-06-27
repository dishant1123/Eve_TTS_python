"""
function  : 

1. no arg no return 
2. with arg no return
3. no arg  with return
4. with arg with return

in python function  declaration  with def  keyword. 
"""

# ex :1  no arg  no return
"""
def hello():
    print(f'hello guys how are you????')
"""

# ex :2  with arg  no return

"""def hello(name):  # name 
    print(f'heyy {name} how are you  ????')
    
hello('jyot')  # what is  parameter and  arg ??? 
"""
# ex :3  no arg  with return

"""def hello():
    return f'hello guys how are you????'
print(hello())
"""
# ex :4  with arg  with return

def sum_two(a,b):
    return a+b

print(sum_two(1,2))
print(sum_two(12.67,24.67))
print(sum_two("jyot","pandya"))

