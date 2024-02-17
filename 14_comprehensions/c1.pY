# comprehensions: provides a concise and readable way to create lists,dict & sets using a more expressive syntax than traditional loops.
#Allows you to generate collections based on existing collections
# list comprehension
#syntax = [expression for item in iterable if condition] # we can add multiple if conditions

# set comprehension
# dict comprehension

L1=[i for i in range(1,10)]
print(L1)


L2=[i**3 for i in range(1,10)]
print(L2)

L3=[i  for i in range(0,30) if i%2==0 if i%5==0]
print(L3)

names = ["admin","not admin","admin","admin","admin"]
l4= [i if i=="admin" else "not admin" for i in names]
print(l4)

L5=[x*y for x in [10,20,30] for y in [10,20,30]]
print(L5)

