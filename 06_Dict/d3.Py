# Pop method to display value afte deleting the key
d1={'a':10,'b':20,'c':30,'d':40,'e':50}
print(d1.pop('c'))  #30
print(d1)           #d1={'a': 10, 'b': 20, 'd': 40, 'e': 50}

del d1['a']
print(d1)            #{'b': 20, 'd': 40, 'e': 50}

#updating the key in dictionary
d2={'a':10,'b':20,'c':30,'d':40,'e':50}
d2['x']=d2.pop('a')
print(d2)                #{'b': 20, 'c': 30, 'd': 40, 'e': 50, 'x': 10}
