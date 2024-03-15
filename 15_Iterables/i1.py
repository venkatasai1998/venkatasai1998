#Iterator
# Itearor is an object
#L1=[]
#print(dir(L1)) #'__iter__'

# private method 
# l1=[10,20,30,40,50]
# L=l1.__iter__()
# print(L)          #<list_iterator object at 0x000001BB08975840>
# print(L.__next__())
# print(type(L.__next__()))    #<class 'int'>
# print(L.__next__())
# print(L.__next__())
# print(L.__next__())     #50
# #print(L.__next__())    #StopIteration

# build in method
# l1=[10,20,30,40,50]
# r1=iter(l1)
# print(r1)
# n1=next(r1)
# print(n1)
# n1=next(r1)
# print(n1)
# n1=next(r1)
# print(n1)
# n1=next(r1)
# print(n1)
# n1=next(r1)
# print(n1)
# n1=next(r1)
# print(n1)


# using loop
L3=[10,20,30,40,50,60,70]
result=L3.__iter__()
print(result)
n1=next(result)
print(n1)
n1=next(result)
print(n1)
n1=next(result)
print(n1)

