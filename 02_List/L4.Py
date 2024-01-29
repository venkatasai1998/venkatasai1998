# List methods
# Empty List

l1=[]
print(l1)

# Append method using to adding the data at the end of the list

L1=[20,30,50,80]
L1.append(100)
print(L1)

L2=["sai",30,50,80]
L2.append("Kumar")
print(L2)


# Extend

L3=([70])
L3.extend([10,20,30,40,50,60])
print(L3)

L4=[]
L4.extend("sai kumar")
print(L4)

L5=[]
L5.extend("sai kumar","venkata sai","rajesh")
print(L5)


# L5.extend("sai kumar","venkata sai","rajesh")
# TypeError: list.extend() takes exactly one argument (3 given)

L6=[]
L6.extend(("sai kumar","venkata sai","rajesh"))
print(L6)