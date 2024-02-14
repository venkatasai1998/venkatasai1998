# def d1(func):

#     def d2(a,b):

#         return print(func(a+b))
    
#     return d2


# def d3(c):

#     return c

# d=d1(d3)
# d(20,20)

# @d1
# def d4(d):

#     return d

# d4(10,10)



def d1(a):

    def d2(username,password):

        if username=="Admin" and password=="Admin":
            return"welcome",username,a
        elif username=="support" and password=="support":
            return"welcome",username,a
        else:
            return"Invaild credentials"
        
    return d2
def d3(c):

    return c

d=d1(d3)
print (d("Admin","Admin"))






