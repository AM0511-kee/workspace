"""# user often provide info so we need to get info from user by using input
#input() are used to provide weather the give data type is same as expected
try:
    x=int(input("enter the value :"))
    print(x)
except Exception:
    print("invalid entry")
    
#getting list as input:

my_list=[]
x=int(input("how many elemet you wanted to add in list:"))
for i in range (0,x):
    element=int(input())
    my_list.append(element)
print("list:",my_list)"""

#getting list using exceptional handling:

try:
    lst=[]
    x=(int(input("number of element:")))
    for i in range(1,x):
        element=(int(input("enter an integer")))
        lst.append(element)
#print(lst)
except ValueError as e:
    print("invalid entry",e)
    
print(lst)
