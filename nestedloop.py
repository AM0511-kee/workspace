#used to print patterns
#first loop is for rows and secound loop is for column
#to print below pattern:
#####
#####
#####
#####
#####
for i in range(5):
    for j in range(5):
        print("#",end='')
    print("\r")
    
#to print * pattern
#*
#**
#***
#****
#*****
n=5
for i in range(1,n+1):
    for j in range(i):
        print('*',end='')
    print('\r')

n=5
for i in range(n,0,-1):
    for j in range(i):
        print('*',end='')
    print('\r')
    
#now lets print a pattern 
'''    *
      **
     ***
    ****
   *****
  ******'''
 

 
n=6
k=2*n-2
for i in range(0,n):
    for j in range(0,k):
        print(end=" ")
    k=k-2
    for j in range(0,i):
        print("*",end=" ")
    print("\r")
    
""" 
    *
   * *
  * * *
 * * * * 
* * * * *
          """
n=5
k=n-1
for i in range(0,n):
    for j in range(0,k):
        print(end=" ")
    k=k-1
    for j in range(0,i):
        print(i,end=" ")
    print("\r")
    
n=5
k=n-1
for i in range (0,n):
    for j in range(0,k):
        print(end=" ")
    k=k-1
    m=1
    for j in range(0,i):
        print(m,end=" ")
        m+=1
    print("\r")


n=6
k=2*n-1
w=1

for i in range(0,n):
    for j in range(0,k):
        print(end=" ")
    k=k-2
    
    for j in range(0,i):
        print(w, end=" ")
        w=w+1
    print("\r")
    
#print alphabets
n=5
num=65

for i in range(0,n):
    for j in range (0,i):
        ch=chr(num)
        print(ch,end=' ')
        num=num+1
    print('\r')