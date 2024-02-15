 # recursion
 # the function calling by itself in order to solve smaller instances in same problem.

# i=0
# def d1():

#     global i
#     i+=1

#     print("d1 function",i)
#     d1()                   #  [Previous line repeated 996 more times]  RecursionError: maximum recursion depth exceeded

     
# d1()

# import sys

# s= sys.getrecursionlimit()
# print(s)          #1000



# s1=sys.setrecursionlimit(1500)
# s2=sys.getrecursionlimit()
# print(s2)


# i=0
# def d1():

#     global i
#     i+=1

#     print("d1 function",i)
#     d1()                   #  [Previous line repeated 996 more times]  RecursionError: maximum recursion depth exceeded

     
# d1()



def factorial(n):

    if n==1:

        print(n)
        return 1
    
    else:
        print(n)
        return n * factorial(n-1)
    
r=factorial(5)
print(r)