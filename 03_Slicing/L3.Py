# adding elements using slicing

L1 = [1,2,3,4,5,6,7,8]
L1[0:1] = [10,20]
print(L1)
print(len(L1[0:1]))

L2 = [1,2,3,4,5,6,7,8]
L2[1:2] = [10]
print(L2)
print(len(L2))

# delete method

L5=[10,20,30,40,50,60,70]
del (L5[6])
print(L5)

# delete element using slicing
L5=[10,20,30,40,50]
L5= L5[:3] + L5[4:]
print(L5)
