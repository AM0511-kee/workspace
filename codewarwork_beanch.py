def filter(l):
    new_list=[i for i in l if type(i)==int]
    print(new_list)
    
filter([1,'a','b',0,15])