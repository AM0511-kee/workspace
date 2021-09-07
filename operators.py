#all and any operator in python
lis1=[]
lis2=[]
for i in range (1,11):
    lis1.append(i*3)
for i in range (0,10):
    lis2.append(lis1[i]%2==0)
print(lis1)
print(lis2)
    
print(any(lis2))

l1=[]
l2=[]
for i in range(0,10):
    l1.append(i**2)
for i in range(0,9):
    l2.append(l1[i]%2==0)

print(l1)
print(l2)
print(all(l2)) 
#operator function
import operator as op 
a=6
b=7
print(op.add(a,b))
print(op.sub(a, b))
print(op.mul(a, b))
print(op.floordiv(a, b))
print(op.truediv(a, b))
print(op.ge(a, b))
#python membership & identifier operator
# is operator and is not operator are membership operator
#in operator and not in operator are identifier operator



 
    