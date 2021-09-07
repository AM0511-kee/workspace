#if statement
#if statement execute a statement only its true else doesn't
i=int(input("get from user :"))
if i<=10:
    i=i+10
    print(i)
print("%d is greater than 10"%(i))

#if else ststement are used to make make either of choice
i=int(input("get from user :"))
if i<=10:
    i=i+10
    print(i)  
else:
    print("%d is greater than 10"%(i))

#nested if statement allows you to have condition statement with in a condition statement
i=int(input("enter the value bugga:"))
if i <20:
    print("%d is less then 20"%(i))
    if i <15 and i <10:
        print("%d is less then 15 and 10"%(i))
    if i<15 and i>10:
        print("%d is less than 15 but greater then 10"%(i))
else:
    print("%d is greater thn 20"%(i) )


#if-elif else statement can be used when there is a multiple choice for if statement
i=input("enter any key:")
if type(i) is integer ==True:
    print ("%d is an int"%(i))
elif type(i) is str == True:
    print("%s is an string"%(i))
else:
    print ("it neither integer nor string")