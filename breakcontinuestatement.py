"""break statement will break out of the loop"""
x=int(input('how many candies do you want:'))
av=10
i=1
while i <=x:
    if i>av:
        break
    print ('candy')
    i+=1
print("bye")

"""continue statement is to skip the next comment line but stays with in the loop"""
x=int(input("print till with number:"))
for i in range (1,x):
    if i%3==0 or i%5==0:
        continue
    print(i)
    
"""pass statement is used to give a empty fun  body"""     
for i in range (1,30):
    if i%2 !=0:
        pass
    else:
        print(i)