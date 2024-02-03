# Range

r1=range(10)
print(r1)       #range(0(start), 10(end), stepover(default 1))

print(list(r1))

r2=range(0,20,2)
print(list(r2))

r3=range(0,20,3)
print(tuple(r3))

r4=range(0,20,2)
print(set(r4))

#r5=range(2,20,2)
#print(dict(r5)) #TypeError: cannot convert dictionary update sequence element #0 to a sequence

l1=[]
l1.extend(r3)
print(l1)      # iterating the data