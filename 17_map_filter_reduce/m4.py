# reduce is a part of "functool" moduke.

from functools import reduce

# L1=[12,32,32,42]
# r=reduce(lambda x,y:x+y,L1)
# print(r)

L2=[12,32,22,13]
r=reduce(lambda x,y:x if (x>y)else y,L2)
print(r)

