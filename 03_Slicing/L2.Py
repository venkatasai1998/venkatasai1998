# slicing with negative indeing
# start : stop(-1) : stepover(default  -1)

L1=[10,20,30,40,50,60,70,80,90,100,110,120,130]
#  -13 -12 -11 -10 -9 -8 -7 -6 -5 -4 -3 -2 -1    

L1.sort()
print(L1)

L2=[10,20,30,40,50,60,70,80,90,100,110,120,130]
L2.sort(reverse=True)
print(L2)


# start is always starting with negative big number
print(L1[-1:])
print(L1[-13:])
print(L1[-13:-10])
print(L1[::-1])

print(L1[::-2])

print(L1[-6:-10:-1])


