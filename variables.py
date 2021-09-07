#variable are storages in memory for a values of certain data type
#variable has scopes 
#scopes are access area for a variable
#to unpack elements for a list we use *
v=[2,45,78,98]
def take_value(a,b,c,d):
    print(a,b,c,d)
take_value(*v)
arg=[1,10]
print(list(range(*arg)))
# * is used to pack and  unpack the list
def fun1(a,b,c):
    print('a=%s,b=%s,c=%s' %(a,b,c))
    
def fun2(*bring1):
     bring1=list(bring1)
     
     bring1[0]='naa tha da'
     bring1[1]='i will be the greatest'
     print(bring1)
     fun1(*bring1) 
     
bring1=('aravind','to','no_matter_what')
fun2(*bring1)
#packing and un packing using **

def func1(**d):
    for key in d:
        print("%s=%s"%(key,d[key]))
        
func1(a='what',b='yours',c='self',d='enough')

#type conversion
x='10001'
print(int(x,2))
print(float(x))
print(str(x))
print(int(x))
    
