def d1(arg):

    def d2():

        return "Hello",arg
    
    return d2

# without decorator
def d3():
    return "Hi"

d=d1(d3())

print(d())

# with decorator

@d1
def d4():

    return "Hey"

d4()

print(d4())



