#any thing which can be looped over is called iterable
#when being iterated iterator are formed
#iterators are basically a state which knows its postion during a iteration
lis=[1,45,65,78,89,99,90]
print(dir(lis))
i_lis=iter(lis)
print(dir(i_lis))
print(next(i_lis))
print(next(i_lis))
print(next(i_lis))
while True:
    try:
        i=next(i_lis)
        print(i)
    except StopIteration:
        break
    
class myrange:
    def __init__(self,start,end):
        self.value=start
        self.end=end
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.value>=self.end:
            raise StopIteration
        current_value=self.value
        self.value+=1
        return current_value
    
def my_range(start,end):
    current=start
    while current<end:
        yield(current)
        current+=1
        
num2=my_range(1,6) 
print(next(num2))
for num in num2:
    print(num) 
            
num1=myrange(1,20)
print(next(num1))
for num in num1:
    print(num)
        

    

        