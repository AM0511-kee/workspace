#iterate using while loop and for loop
c=0
while c<5:
    print(c)
    c+=1    
#while loop need a counter and an iterator for working
# loop can be used with indexes for that we need to find len() of lst
lst=['greek','for','greek','what','ever','it','takes']
for index in range (len(lst)):
    print(lst[index])

#ennumurate in python is used to loop over a container with the [index] and value[indexes]
for key, value in enumerate(['greek','value','what','ever']):
    print(key,value)
#zip() is used to combine values of two containers
q=['name','age','gender']
a=['aravind','22','male']
for i,j in zip(q,a):
    print("what is your{0}:{1}".format(i,j)) 
    
#not using 
def lop(**kwarg):
    for key in kwarg:
        print("%s=%s"%(key,kwarg[key]))
lop(val='dic',val1='fro',val2='kob')
#you can loop over an container using enumerate
#both items,iteritem are used to iterate over dictinory
#zip()meathod is used to zip two containers
#sorted() is also used to iterate over container
#set()will eliminate all the duplicate value
dic={'name':'kevin','age':'23','personality':'great humanbeing'}
for i,j in dic.items():
    print('%s=%s'%(i,j))
    
lt=[1,24,56,54,34,66,78,98,100]
for i in sorted(set(lt)):
    print(i)
#reverse is used to set the list in reverse order
for i in reversed(lt):
    print(i,end=' ')
    
for i in reversed(range(1,10,2)):
    print(i,end=' ')