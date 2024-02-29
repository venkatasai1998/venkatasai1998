#polymorphism
# method overloading (implementation no : because of security issues,explicity we can implement by importing dispatch method)
# method overriding
# constructor overloading
# operator overloading

from multipledispatch import dispatch

class product:
    @dispatch(int,int)  # by using dispatch method users can try to setup their fixed datatypes while calling the objects.
    def d1(self,a,b):

        print(a,b)
    @dispatch(str,int)

    def d2(self,a,b):

        print(a,b)

p=product()
p.d1(10,20)
p.d2("sai",30)



