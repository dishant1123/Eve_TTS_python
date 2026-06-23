# set : mutable  set  of  unique  elements  and unordered not repeation allowed in set. 

"""
s1={100,10,1,2,3,4,5,6,70,8,9,10,10,10}
print(s1)
print(type(s1))
"""

# not access though index , no slicing possible  in set and  not  changes though the index. 
"""
s1={100,10,1,2,3,4,5,6,70,8,9,10,10,10}

print(s1[0])
s1[8] =900  # not  possible
print(s1)
"""

# built in function  : len  min max sorted

"""
s1={100,10,1,2,3,4,5,6,70,8,9,10,10,10}

print(len(s1))
print(min(s1))
print(max(s1))
print(sorted(s1))
"""
#convert to list :
"""
s1={100,10,1,2,3,4,5,6,70,8,9,10,10,10}
list_of_elements = list(s1)  # convert  set  to  list  and  print  the  list
print(list_of_elements)
"""

# method : 
"""s1={1000,10,18,2,3,4,5,6,700,8,9,10,10,10}
print(s1)

s1.add(200)
print(s1)

s1.clear()
print(s1)

s2 =s1.copy()
print(s2)

s1.remove(10000)  # if element not  in set then  it given error
print(s1)

s1.discard(10000)# if element not  in set then  it given same set.
print(s1)

s1.pop()  # remove the last element  from the set
print(s1)
"""

# union , intersection , difference , symmetric_difference , issubset , issuperset : 

# s1={1,2,3,4,5}
# s2={4,5}
# s3={1,2,3,4,5,6,7,8,9,89}

# print(s1.union(s2))
# print(s1.intersection(s2))
# print(s1.difference(s2))  # s1-s2 

# print(s1.symmetric_difference(s2))  # s1-s2  ==> print remaining element for both set. 

#update  : 
"""s1={1,20,3,4,5}
s2={"vyom"}

s1.update(s2)
print(s1)
"""

# frozen set: immutable set  and  not  changes  in  the  set .

"""fz = frozenset([1,2,3,4,5,6,7,8,9,10,1])
print(fz)
print(type(fz))

"""