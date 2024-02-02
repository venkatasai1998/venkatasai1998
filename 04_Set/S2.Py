#add()
S1=set()
print(S1,type(S1)) #{10} <class 'set'>


S1.add(10)
S1.add(20)
print(S1)

#S2={}
#S2.add(10)
#S2.add(20)
#print(S2)  #AttributeError: 'dict' object has no attribute 'add'

S3={10,20,30,40}
S3.pop()
print(S3) #{10, 20, 30}

S3.pop()
print(S3) # {20, 30}

S3.pop()
print(S3) # {30}

S3.pop()
print(S3) # set()

S3.pop()
print(S3) #KeyError: 'pop from an empty set'





