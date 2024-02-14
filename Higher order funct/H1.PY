# Higher order functions
# The function that takes as an argument and returns a function when called

# def d1():

#     print("d1 function")

#     def d2():

#      print("d2 function")
    

#     return d2

# d=d1()   #  taking coonnection of d2 using d as a variable nothing but d=d2;
# print(d)
# d()
# print(d.__name__)


def d1(a):

    def d2(b):

      return a+b  
    
    return d2
    
d=d1(20)
d(20)
print(d(20))







