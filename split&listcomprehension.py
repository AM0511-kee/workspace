#split is used to split the string to get multiple input
#split a string using .split(seperator,no.of split)
x,y=input("enter the value").split()
print("x=",x)
print("y=",y)
print()
#split to get three value
x,y,z=input(("enter the values:")).split(",",2)
print("x=",x)
print("y=",y)
print("z=",z)
#list comperence is same as split but it can take multiple vale and form a list we use [] as we use for list
x=[int(x) for x in input("enter multiple element:").split()]
print("the list is",x)

y=[int(y) for y in input("enter the elements").split()]
print("list:",y)
