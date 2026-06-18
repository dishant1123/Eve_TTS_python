"""
task :1
ask user to enter the number  append  in the  list  and  second  largest number in list.
input  : l1 =[12,34,56,78,23,12]
output : second largest number  is  : 56

task :2 ask user to enter the number  append  in the  list  and  print the  prime number in seprate list. 

input  : l1= [1,2,3,4,5,6]
output : result =[2,3,5]

task :3 ask user to enter the number  append  in the  list  and  print the  pelidrome number in seprate list. 

input  : l1= [121,131,145,678,9000]
output : result =[121,131]

task :4 ask user to enter the number  append  in the  list  and  print the  reverse number in seprate list. 

input  : l1= [123,135,145,678,9001]
output : result =[321,531,541,876,1009]


"""

l1 =[12,34,56,78,23,12]

sorted_l1 = sorted(l1)
second_largest = sorted_l1[-2]
print("sorted list is: ",sorted_l1)
print("second largest number  is  :",second_largest)
