#try used to try and execute the statement
#except satement is used to except the error an dprint the error message
#we can use 'else' statement along with exception statement it will be executed only if exception statement is not executed
#finally keyword is used to execute all the statement below it



# try:
#     a=10
#     b=10
#     c=((a+b)/(a-b))

# except ZeroDivisionError as e:
#     print(e)
    
# else:
#     print('the answer is %i'%(c))

# finally:
#     print('program got executed')
    

#user defined exception are used create your own exception by using class with inhertiate exception as super class

class ara_error(Exception):
    def __init__(self,value):
        self.value=value
        
    def out_put(self):
        return (self.value)
    
try:
    raise(ara_error(9))

except ara_error as error:
    print('the value of buildin error is ',error.value)
    
finally:
    print('execution')
















