def outerfunc(a):
    messege=a
    def innerfunc():
        print(messege)
    return innerfunc #function is returned 
out=outerfunc('hello')
print(out.__name__)
out()

#closures using func as parameter
def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y
def div(x,y):
    return x/y        

def outer_func(func):
    def inner_func(*arg):
        print(func(*arg))
    return inner_func
fun=outer_func(add)
print(fun.__name__)
fun(99,78)

#decorators takes func as an agruments, add functionality with out altering exting code.
def decorator_function(orginal_function):
    def wrapper_function(*arg,**kargu):
        print("decorator_function is executed before {}".format(orginal_function.__name__))
        return orginal_function(*arg,**kargu)
    return wrapper_function

@decorator_function
def display(message):
    print(message)
    
# dec=decorator_function(display)
# print(dec)
# dec()
     
display("whatever it takes")

def decorator_function(func):
    def inner_function(*arg,**kwarg):
        print("decorator function is executed before{}".format(func.__name__))
        return func(*arg,**kwarg)   
    return inner_function
        
                
def addtion(x,y):
    print(x+y)  
    
sum=decorator_function(addtion)
print(sum)
sum(20,10)

#decorators add additional funcnality to a function without distrubing the original code
def decorator_function(*arg,**kwarg):#decorator function
    print('decorator function is executed ')
    def wrapper_function(func):#wrapper function
        print('before executing wrapper function')
        for i in arg:
            print('i like',i)#argumnents is used to pass arg
        func()
    return wrapper_function 
        
@decorator_function('kevin','chocolate','chocolate icecream','appa','amma','expensive things')        
def no_arg(): #function
    print("this function does n't take any argument")
    
#decorator for executing two difference function
def outer_decorator_func(datatype,message1,message2):
    print(message1)
    def decorator_function(func):#function inside a function
        print(message2)
        def wrapper_function(*args,**kwargs):#wrapper function
            if all([type(arg)==datatype for arg in args]):
                return func(*args,**kwargs)#returning the execution of function
            return ('invalid input')
            
        return wrapper_function
    return decorator_function        

@outer_decorator_func(str,'inside outer decorator function' ,'inside decorator function')
def str_concatination(*args):
    st=" "
    for arg in args:
        st+=arg
    print (st)
@outer_decorator_func(int,'inside outer decorator function','before sum of all the elements')    
def int_sum(*args):
    sum=0
    for arg in args:
        sum+=arg
    print(sum) 
    
str_concatination('whatever','it','takes','im','the','champ','the greatest','im earning it')
int_sum(10,30,40,50,60,80,56,78,65)

#memoization stores the value of expensive computer call, 
#and return the cached result, when the same function with same value is being called
#memoization is an optimizing computer program
def memoization(func):
    memory={}
    def inner(num):
        if num not in memory:
            memory[num]=func(num)
        return memory[num]
    return inner
@memoization


def fac(num):
    if num==1:
        return 1
    return num*fac(num-1)
#fac=memoization((fac))
print(fac(15))

#range finction does not return itertor
demo=iter(range(1,10))
print(demo)
for i in demo:
    print(i)
    
print(demo.start)

#test for decorators:
#decorators for two different function

def outer_function(datatype,message1,message2):
    print(message1)
    def inner_function(func):
        print(message2)
        def wrapper_function(*args,**kwargs):
            if all([type(arg)==datatype for arg in args]):
                return func(*args,*kwargs)
            return 'invalid datatype'
        return wrapper_function
    return inner_function
@outer_function(str,'we dit it', 'you are a programmer now')
def str_data(*args):
    st=' '
    for arg in args:
        st+=arg
    print(st)
@outer_function(int,'it is what itis','man you are the luckiest kid ever lived')  
def int_data(*args):
    i=0
    for arg in args:
        i+=arg
    print(i)
    
    
str_data('naa','','raja',' ','naa','','raja',' ','eppothu',' ','naa','','raja')
int_data(10,30,50,68,33,20,19,17,22)