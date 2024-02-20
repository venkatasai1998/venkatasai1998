# l1=[1,2,3,4]
# l2=[1,2,3,4]
# print(l1 * l2)  # TypeError: can't multiply sequence by non-int of type 'list'

# l1=[1,2,3,4]
# l2=[1,2,3,4]

# def d1(a,b):

#     return a+b

# d=map(d1,l1,l2)
# print(list(d))  #[2, 4, 6, 8]

l1=[1,2,3,4]
l2=[1,2,3,4]
(print(list(map(lambda a,b :a+b,l1,l2))))   #[2, 4, 6, 8]
