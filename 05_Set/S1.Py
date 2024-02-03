# set default value is set()
# when you are passing values into set() it will take set{} as a constructor

S5={10}
print(S5,type(S5))


S1 = {1, 2, 3, 4, 5}
S1.add(6)
print(S1)

S2 = {1, 2, 3, 4, 5}
S2.remove(2)
print(S2)

S3 = {4, 5}
S4= {1, 2, 3}
union_set=S3.union(S4)
print(union_set)


S7={10,20,30,40,50,60,70,80,10,50,30}
print(S7, type(S7))  #{70, 40, 10, 80, 50, 20, 60, 30} <class 'set'> unordered and doesn't allow duplicate values

# Remove duplicates in a list using sort

L1=[10,20,30,40,10,20,30,40]
print(L1)

S9=set(L1)
print(S9)

L2=list(S9)
L2.sort()
print(L2 )


S10={'one','two','three','four','five','six'}
S10.remove('one')
print(S10)
print(S10)

S11={'one','two','three','four','five','six'}
S11.discard('one')
print(S11)
print(S11)

#S10.remove('seven')
#print(S10)  #KeyError: 'seven'

S11.discard('eight')
print(S11)