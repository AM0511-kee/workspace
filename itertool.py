import itertools
import operator
# infinte iterator can go on forever
# itertool.count(),itertools.cycle(),itertools.repeat() are some of example of infinate iteration function
#itertool.zip_longest is used to iterate for longest possible value
counter=itertools.count(start=1,step=1)
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
lst=[1,23,45,67,78]
v=print(list(zip(itertools.count(),lst)))
w=print(list(itertools.zip_longest(range(0,10),lst)))
cycles=itertools.cycle(("on","off"))
print(next(cycles))
print(next(cycles))
print(next(cycles))
print(next(cycles))
print(next(cycles))
rep=itertools.repeat(2,times=2)
print(next(rep))
print(next(rep))
print(next(rep))
print(next(rep))
print(next(rep))
m_p=map(lambda x : x+x ,range(10))
print(list(m_p))
print(list(itertools.starmap(pow,[(0,2),(1,2),(2,2),(3,2),(4,2)])))
#combination doesn't bother about order of elements
numbers=[1,2,3,4,5,6]
c=itertools.permutations(numbers, 2)
for i in c:
    print(i)
    
#permutation cares about order 
#repeat function allows repeatation of elements
numbers=[1,2,3,4,5,6] 
c=itertools.product(numbers,repeat=4)
for i in c:
    print(i)
    
w=itertools.combinations_with_replacement(numbers,5) 
for i in w:
    print(i) 
    
#chain function is used to combine two or more list
numbers=[1,2,3,4,5,6] 
alphabet=['a','b','c','d','e','f','g','h','j']
words=['aravind','kevin','gugan']
combined=itertools.chain(numbers,alphabet,words)
for i in combined:
    print(i,end=" ")
    
#compress function works similarly like filter function but it return value that are true in selector list
#or else it returns false and it will not valuate the value

alphabet=['a','b','c','d','e','f','g']
selectors=['true','true','false','true','false','false','true']
p=itertools.compress(alphabet, selectors)
print('\n',next(p))
for item in p:
    print(item)
    
num=[10,34,52,76,45,65,98,100,200,156,67]
def lsts(i):
    if i <60:
        return True
    return False
p=filter(lsts,num)
print(next(p))
for i in p:
    print(i)
p1=itertools.filterfalse(lsts,num)
print(next(p1))
for i in p1:
    print(i,end=' ')
#accumulate is used to perform operation on every element in iterable
num=[10,34,52,76,45,65,98,100,200,156,67]
c_b=itertools.accumulate(num)
print(next(c_b))
for i in c_b:
    print(i,end=' ')
a_c=itertools.accumulate(num,operator.mul)
for i in a_c:
    print(i,end=" ")
    
#group_by function works same as group_by function in sql
#groups objects on the bases of arguments

people=[
    {'name':'aravind',
     'age':'22',
     'city':'chennai'},
    {'name':'kevin',
     'age':'22',
     'city':'arakomam'},
    {'name':'yaser',
     'age':'21',
     'city':'chennai'},
    {'name':'hema kumar',
     'age':'22',
     'city':'arakonam'},
    {'name':'jaga bro',
     'age':'22',
     'city':'palakadu'},
    {'name':'mani kandan',
     'age':'22',
     'city':'dhindivanam'}
] 

#for a group_by function need an function that describe arguments on which the group_by meathod need to group 

def person_city(person):
    return person['city']

g_b=itertools.groupby(people,person_city)
       
for key,group in g_b:
    print(key)
    for person in group:
        print(person)
    print()
def sort_city(person):
    return person['city']
    
g_b=itertools.groupby(people,sort_city)

for key,group in g_b:
    print(key)
    for person in group:
        print(person)
    print()
def key_fun(person):
    return person['age']

third_attem=itertools.groupby(people,key_fun)

for key,group in third_attem:
    print(key)
    for person in group:
        print(person)
    print()

