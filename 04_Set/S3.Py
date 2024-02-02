# frozenset
F1= frozenset()
print(F1,type(F1))

# Adding the set into the frozenset
s1={10,20,30,40,50}
f2=frozenset(s1)
print(f2)       #frozenset({50, 20, 40, 10, 30})

# Adding frozenset into the set
f3=frozenset({50, 20, 40, 10, 30})
s2={'Name one'}
s2.update(f3)
print(s2)      #{50, 20, 40, 10, 'Name one', 30}




