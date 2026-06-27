"""
function  :

1. no arg no return 
2. with arg no return
3. no arg  with return
4. with arg with return

in python function  declaration  with def  keyword. 
"""

# ex :1 

"""def hello():
    print(f'hello guys how are you????')
    
hello()
print("heeeee")
hello()
"""

"""s = ["foo" ,"ram"]
s[0] = 'b'
print(s)
"""
# print(s[0])

s = "Python"
s = (s[ : : -2]) # n h y 
print(s[-1])

tup = (1, 2, (3, 4, (5, 6,7)))
#      0  1     2    ===> 3 4  (5 6 7)
print(tup[0])

d = {}
d[1] = 'a'
# d[True] = 'b'  #  d[1]='b'
print(d)

d2 ={'phy' :90 , 'che' :89}

d2['phy'] =99
print(d2)

a = {1, 2, 3}
b = {2, 3, 4}
print(a & b)  # intersection 
print(a and b)  #

for i in range(10):
    if i == 5:
        continue
    else:
            print(i)
else:
      print("Here")  