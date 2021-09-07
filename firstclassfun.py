#first class function is that function are treated as any other object or variable
#like we can store an function to an variable

def f_c(i):
    return (i+i)
f=f_c(2)#func calling
print(f)
g=f_c #storing a function to a variable
print(g)

#higher order function are when function are passed as an arguments ,or func returns func as an result 
#map are best example of higher order function 
#map takes func as an argument and list as arguments
#map apply a certain function to evey elemnt in a list and return the value
def sqr(i):
    return i*i

e=map(sqr,[1,3,5,7,8,10,15,18])
print(next(e))
for n in e:
    print(n)
print(e)

#closure

def closure(arg):
    def inner(msg):
        return('<{0}>{1}<{0}>'.format(arg,msg))
    return inner
c1=closure('hi')
print(c1('tha yaru da itha loosu kooo'))
  
def outer_func(arg):
    def inner_func(msg):
        print('<{0}>{1} <{0}>'.format(arg,msg))
    return inner_func

clo1=outer_func('hi')
clo1('what ever it is')

def funct(func):
    def argumens(*arg):
        print(func(*arg))
    return argumens #returns function as an argument

def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y
add_arg=funct(add)
sub_arg=funct(sub)
mul_arg=funct(mul)
mul_arg(70,90)
print(add_arg)
add_arg(4,8)
    
    