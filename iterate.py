#iterate are used to loop over a particular container
l=['KTM','kawasaki','yamaha']
for x in l:
    print(x)
for i in range(len(l)):
    print(l[i])
for i,j in enumerate(l):
    print(i,j)
    
print(list(enumerate(l)))
#enumarate can be used to loop over to containers
brand=['KTM','YAMAHA','BMW']
parts=['shock absorber','rim','service'] 

pricing={0:'2,00000',1:'1,50000',2:'3,00,000',
         3:'5000',4:'3000',5:'2500'}
for index,x in enumerate(brand):
    print('%s cost=%s'%(x,pricing[index]))
for index,y in enumerate(parts):
    print('%s cost= %s'%(y,pricing[index+len(brand)]))
    
brand=["ev","bdh","mnnnn"]
print(brand[len(brand)-1])

print("make happiness your priority")