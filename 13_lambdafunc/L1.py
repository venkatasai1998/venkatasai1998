# def d1():

#     return print("d1 function")

# d1()


# L1=lambda : print("lambda function")

# L1()

# def d2(a):

#     return print("d2 function: ", a )


# d2(20)



# L2=lambda a:print ("lambda function: ", a )

# (L2(30))

# task 3

# def d4(a,b):

#     return print(a+b)

# d4(5,10)


# l4=lambda a=5,b=10:a+b
# print(l4(100,200)) # the original value will try to change


# task 4
# lambda for higher order functions

def d1(a):

    def d2(b):

        return a+b
    return d2

d=d1(10)
print(d(5))

L3=lambda a: (lambda b : (a+b))

L=L3(25)
print(L(25))



