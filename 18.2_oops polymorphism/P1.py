#polymorphism: has many forms(length is the best example for polymorphism)
# method overloading (implementation no : because of security issues,explicity we can implement by importing dispatch method)
# method overriding
# constructor overloading
# operator overloading


# method overloading
from multipledispatch import dispatch

class product:
    @dispatch(int,int)  # by using dispatch method users can try to setup their fixed dagit tatypes while calling the objects.
    def d1(self,a,b):

        print(a,b)

    @dispatch(str,int)
    
    def d2(self,a,b):

        print(a,b)

p=product()
p.d1(10,20)
p.d2("sai",30)

#constructor overloading

from multipledispatch import dispatch

class datatypes:
    @dispatch(int,int)

    def __init__(self,a,b) :

        print("spaecial method 1 :", a,b)
    @dispatch(int,str)

    def __init__(self,a,b) :

        print("spaecial method 2 :", a,b)
    @dispatch(str,int)

    def __init__(self,a,b) :

        print("spaecial method 3 :", a,b)     #spaecial method 3 : 10 20(highest priority while calling class without dispatch method)

datatypes(10,20)
datatypes("sai",10)
datatypes(10,"sai")



