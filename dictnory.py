#dictory is key value pair
dic={1:'nedd',2:'val',3:'nhhh'}
dic1=dict([(1,5),(2,'val'),(3,'nhhh')])
print(dic1)
#creating a dictnory using dict()

print(dict([(1,'a'),(2,'be'),(3,'naaa')]))
#nested dict
nested=dict([(1,'aravind'),(2,'kevin'),(3,((4,'jaga bro'),(5,'ganesh bro'),(6,'nested')))])
print(nested)
#creating a nested dict
nes={1:'value',2:'wave',3:'nifty',4:{5:'nested',6:'da',7:'ithu'}}

#acessing elemen from the dict
print(nes[1])
print(nes[4][5])
nes[7]='set da ithu'

#deleting element
#del nes[4][6]
print(nes.get(4))
print(nes)
print(nes.items())
s="how can mirrors be true is our eyes are fake"
n_s=" ".join(words[0].upper()+words[1:] for words in s.split(" "))
print(n_s)

def fun(strings):
    print (strings.title())
    
fun(s)
    


