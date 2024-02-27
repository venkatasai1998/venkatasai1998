# Grenertors are functions we can create own iterations
# Generator are implemented using functions and yeild keyword
# generators are iterator.

# def d1():
#     return 10
#     return 20
#     return 30
# d = d1()
# print(d,type(d))

# def d1():
#     return 10,20,30

# d=d1()
# print(d,type(d))

# def d1():
#     yield 10
#     yield 20  # we will not use return keyword in the middle of yeild keyword,because it terminates
#     yield 30  

# d=d1()
# print(d)     #<generator object d1 at 0x0000021DA2B34B40>
# print(d.__next__())
# print(d.__next__())
# print(d.__next__())
# print(d.__next__())v

# return
# def d1():
#     yield 10
#     yield 20
#     return 30
#     yield 40

# d = d1()
# print(d)
# print(next(d))
# print(next(d))
# print(next(d))  #StopIteration: 30

# generator comprehension(nothing but tuple comprehension)

# a1=(i for i in range(10))
# print(a1)         #<generator object <genexpr> at 0x000001EFFDA24880>
# print(tuple(a1))





