#OOPS 
# class
# object
# inheritance : Extending properties from one class to another class
# class Superclass:
    # Superclass attributes and methods
# class Subclass(Superclass):
    # Subclass attributes and methods
# polymorphism : 
# Abstraction :process of hiding the complex implementation details and showing only the necessary features of an object. It allows focusing on what an object does rather than how it does it.
# Encapsulation : wrapping the data and their methods into single unit (class)

class Hello:
    pass  #pass denotes a class definition with no explicit content (attributes or methods).

class Hi:

    print("Hello")

class Hey:

    def __init__(self) :       #__init_ denotes special method it automatically calls when you create an object
        print("Hello Friends")

# object
Hey()


class product:

    def __init__(self,productname,productprice):
        print(productname,productprice)

product("samsung",10000)


class services:

    def __init__(self,appleservice,samsungservice,lgservice):

        self.a_service=appleservice
        self.s_service=samsungservice
        self.lg_service=lgservice

        return print(self.a_service,self.s_service,self.lg_service)
        
services("Macbook","samsungflip","washing machine")



class test:

    def __init__(self):     #__new__ magic method , priority is more

        print("Magic method")

    def __new__(self):     # __init__special method

        print("special method")

test()