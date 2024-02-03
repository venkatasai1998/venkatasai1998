d1={'a':10,'b':20,'c':30,'d':40,'e':50}
print(d1)

print(d1.keys())    #dict_keys(['a', 'b', 'c', 'd', 'e'])
print(d1.values())  #dict_values([10, 20, 30, 40, 50])

d4={1:10,2:20,3:30,4:40,5:50}
del d4[1]
print(d4)   #{2: 20, 3: 30, 4: 40, 5: 50}

d5={'pizza':5,'burger':10}
print(d5)
print(d5['burger']+1)
print(d5)

d5['burger']=20
print(d5)