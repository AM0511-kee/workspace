print("select operation :\n"\
    "1. addition \n"\
    "2. subtration \n"\
    "3. multiplication\n"\
    "4. division\n")
choice=int(input("select any option between 1,2,3,4:"))

def firstchoice(a,b):
    print(a+b)

def secoundchoice(a,b):
    result= abs(a-b)
    print(result)
    
def thirdchoice(a,b):
    print (a*b)

def fourthchoice(a,b):
    print(a/b)
   

if choice==1:
    a=int(input("enter the first value:"))
    b=int(input("enter the secound value:"))
    firstchoice(a, b)
elif choice==2:
    a=int(input("enter the first value:"))
    b=int(input("enter the secound value:"))
    secoundchoice(a, b)
elif choice==3:
    a=int(input("enter the first value:"))
    b=int(input("enter the secound value:"))
    thirdchoice(a, b)
elif choice==4:
    a=int(input("enter the first value:"))
    b=int(input("enter the secound value:"))
    fourthchoice(a, b)
else:
    print("choice between 1-4:")
    
#get file statement using print elememt and we get the value
        
    