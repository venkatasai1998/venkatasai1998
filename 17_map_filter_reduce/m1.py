# map() function is used to apply a specified function to each item in an iterable(list,tuple,set) and returns an iterator that yields the results
# syntax : map(function,iterable,.........)

# L1=[10,20,30,40,50]
# print(L1 * 2)

# # map func
# L2=[10,20,30,40,50]
# def d1(n):
#     return n*2

# a=map(d1,L2)     
# print(a)        #<map object at 0x00000241D9C75E10>
# print(tuple(a))


#lamba function synax: Lambda arguments:expression
#map function syntax : map(function,iterable,.........)
print(list(map(lambda n:n*2,[10,20,30,40,50])))  # we can write entire map program in single line