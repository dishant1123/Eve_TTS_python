"""
convert  tuple  in to the  list . 

t1 =(1,2,34,56,78,90)  in t1 tuple add one  element at the end and print  them .

input  : t1 =(1,2,34,56,78,90)
output : t1 =(1,2,34,56,78,90,100)

"""

"""
t1 =(1,2,34,56,78,90)
l1= list(t1)
print(l1)
l1.append(100)
print(tuple(l1))
"""

# dict : key and value  pair  ===> mutable ===< change the value  

"""
d1 ={"phy":90 , "math":78}
print(d1)
print(type(d1))     # phy ==> key  90 value   math ==> key 78 value

d2 ={90:78 , "com":57}
print(d2)  # note  : key  value  pair  order  is  not  important and you take  any data type in key . in this case 90 key and  78 value  
"""
#add ,update: 

# add : add com  in this dict. 
"""
d1 ={"phy":90 , "math":78}
d1['com']=57 
print(d1)
"""
# update  : update the  value  of  key  phy  in this dict.

"""
d1 ={"phy":90 , "math":78}
d1['phy'] =99
print(d1)
"""

# built in function  : len  min max sorted 
"""d1 ={"phy":9 , "math":7}
print(len(d1))
print(min(d1))
print(max(d1))
print(sorted(d1))
"""

# mutiple value  in dict : 

"""d1= {
    "phy" :[91,94,96],
    "math" :[78,80,82],
    "comp" :[57,60,63]
}
print(d1)
print(d1['phy'])

for i ,j in d1.items():
    print(i,j)
"""
# methods : 
# d1 ={"phy":9 , "math":7,90:89}

# d1.clear()
# print(d1)

"""d2 = d1.copy()  # copy() : copy the  dict  and return the copy  dict , not memory shared 
print(d2)
d2['com']=99
print(d1)
print(d2)

d2 =d1   # memory shared    ===> view ()  same as apply in list . 
print(d2)
d1['com']=99
print(d1)
print(d2)
"""
# get  key value  items :
"""
print(d1.get('phy')) # print the value  of key phy

print(d1.keys())
print(d1.values())
print(d1.items())
"""

# pop :

"""
d1 ={"phy":9 , "math":7}
print(d1.pop("phy"))
d1.pop("math")
print(d1)
"""

# fromkeys , update , pop item : 

d2=["ram","sita"]   # ==> d2={"ram":90,"sita":90}

# d3= dict.fromkeys(d2,90)
# print(d3)
# d3["sita"] =89
# print(d3)

# d3.update({"sita":89})
# print(d3)

"""d1 ={"phy":9 , "math":7,'com':90}

print(d1.popitem())  # last key value  remove
print(d1)
"""
# task  :1 
"""
ask user to enter the  3 student name and its marks store in to the dict. 

enter the student : 3 
    enter the name  : ram 
        enter the mark : 90
    enter the name  : sita
        enter the mark : 80
    enter the name  : priyanka
        enter the mark : 85
        
output  : d1 ={"ram":90,"sita":80,"priyanka":85}
"""
"""n=int(input("enter the  nunber of students : "))
d1={}
for i in range(1,n+1):
    name=input("enter the  name : ")
    marks=int(input("enter the  marks : "))
    d1[name] =marks

print(d1)    
"""
"""
task  :1 
print  this pattern  : 

1.          2.           3.       4.             5. 
* * * * *   * * * * *        *        *              *
  * * * *    * * * *       * *       * *            * * 
    * * *     * * *      * * *      * * *          * * *
      * *      * *     * * * *     * * * *        * * * *
        *       *    * * * * *    * * * * *      * * * * *
                                                  * * * * 
                                                   * * * 
                                                    * * 
                                                     *


task :2 
remove the  duplicate  element  from the list  and print  the  list .

input  : l1 =[12,34,56,78,12,12,56,89]
output : l1 =[12,34,56,78,56,89]

task :3 

sort by  second element in the list . 

input  : l1 =[[0,4],[1,2],[6,7]]
output  : l1 =[[1,2],[0,4],[6,7]]

task :4 ask user to enter the  any number and  print  first digit  and  last digit  sum. 
input  :12234 
output : first and  last  digit sum is  : 1+4 =5 

8.Write a program to find duplicate values in a tuple.
    t = (10,20,30,10,40,20,50)
    output  :[10, 20]
9.Find second largest number in a tuple 
    t = (12,45,78,23,90,56)
    output  : 78

"""

"""
task :2 
remove the  duplicate  element  from the list  and print  the  list .

input  : l1 =[12,34,56,78,12,12,56,89]
output : l1 =[12,34,56,78,56,89]

"""
# task :2 
"""
l1 =[12,34,56,78,12,12,56,89]
l2=[] 

for i in l1 : 
    if i not in l2 : 
        l2.append(i)
print(l2)
"""

# task :3
task :3 


l1 =[[0,-4],  #  ===> 0  0 ,4   ===> index 0 ,4 ===>1 
     [1,-1],  #  ===> 1  1,2    ====> index 1  2 ===>1 
     [-6,7]]  #  ===> 2 6,7     ====> index 0 7 ===>1
"""
for i in range(len(l1)):   # 2 ,3 
    for j in range(i+1,len(l1)):  # 3,3 
        if l1[i][1] > l1[j][1]:  # if l1[1][1] > l1[2][1]  2  > 7   
            temp = l1[i]        #    temp=[0,4]
            l1[i] = l1[j]       # l1[0] = [1,2]
            l1[j] = temp        #  l1[1]=[0,4]
            
print(l1)      #  [[1,2] ,[0,4],[6,7]]
"""
print(sorted(l1))  #  