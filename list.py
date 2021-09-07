#create a list by using []and placing the elements in it
#size of a list can be found using len() function
l=['what',40,40.54,0,0.005]
print(len(l))
#add elemnt using append(),insert(),extend()
l.append(30)

l.insert(1,'eat')
l.extend([30,'e','hishsh',28,90])
#extend will take list as an argument
#delete using remove()&pop()
l.remove('e')
l.pop()
l.pop(3)
print(l)
#slice a list using indexes [2:5]
print(l[2:8])
#list can be reversed by using [::-1]
print(l[::-1])
#list comprehension can be used to create a new list using iterate
#nl=[int(x) for x in input("enter the value:").split()]
#print("list :",nl)
nl2=[int(x) for x in range(0,7) if x%2==0]
print(nl2)
#nested list comprehension
l=[]
for i in range (5):
    l.append([])
    for j in range(5):
        l[i].append(j)
print(l)
        
nl=[[j for j in range(5)] for i in range(5)]
print(nl)
lst=[]
for i in range(5):
    lst.append([])
    for j in range(5):
        lst[i].append(j)
print(lst)
nlst=[[ j for j in range(5)] for i in range(5)]
print (nlst)
#list compherence can be divided into three catagory 1st is the object you wannted to append ,secound is the  inner looop,
# 3rd is the outer loop
test=[[j for j in range (5)] for i in range(5)]
print(test)
alst=[[20,30,80],[56,80,99],[67,89,13]]
nalst=[]
for x in alst: 
    for y in x:
        nalst.append(y)
print(nalst)
nlst2=[y for y in x for x in alst]
print(nlst2)
#u can also use list comprehension using if condition as well

lst=[[20,54,44],[20,60,78,42]]
m=[]
for x in lst:
    for i in x:
        if i <50:
            m.append(i)
print(m)

m1 =[i for i in x for x in lst if i<50]
print(m1)
#concatiantion can do in list by using '+', list comprehension,extend()
l1=[20,30,40,58]
l2=[1,23,32,43,5]
for i in l1:
    l2.append(i)
print(l2)
l3=[i for y in [l1,l2] for i in y  ]
print(l3)
l1.extend(l2)
print(l1)
#reduce function in python 
import functools as fu
import itertools as ai  
lst=[4,94,88,43,25,67,98,34,56]
print(fu.reduce(lambda a, b :a+b , lst))
print(ai.accumulate(lst,lambda a,b : a+b))
enumerate(lst)
print(list(enumerate(lst)))
#using enumerate(iterable) in loop
for ele in enumerate(lst):
    print(ele)
for ele,count in enumerate(lst):
    print (count)
    print (ele)
for ele in enumerate(lst,100):
    print(ele)
#filter()is used to check the applied condition for every element in sequence
lst=[10,3,49,85,67,6,4,56,6]       
print(list(filter(lambda a : a%2==0,lst)))
#map() is used to apply a set of operation for each element in sequence
lst=[10,3,49,85,67,6,4,56,6]    
print(list(map(lambda x :x+10,lst)))
#where are what we feel just feel good ,you are blessed as heaven man you can be greater
#man you will get ever thing you want just work to be a best version of u
print("the world value  are in the space")