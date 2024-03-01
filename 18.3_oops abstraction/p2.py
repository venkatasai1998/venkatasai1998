#note: when we declare all the methods as abstract method we can call as interface


# from abc import ABC,abstractmethod

# class parent(ABC):
#     @abstractmethod
    

#     def d1(self):
#         pass

#     @abstractmethod

#     def d2(self):

#         pass
#     @abstractmethod

#     def d2(self):

#         pass
    
# class child (parent):

#     def d1(self):

#         print("d2 method of abs")
#     def d2(self):

#         print("d2 method of abs")

#     def d3(self):

#         print("d2 method of abs")


# c=child()
# c.d1()
# c.d2()
# c.d3()



#task2
from abc import ABC,abstractmethod

class parent(ABC):

    @staticmethod
    @abstractmethod
    def d1():
        pass

    @classmethod
    @abstractmethod
    def d2(cls):
        pass


    @abstractmethod
    def d2(self):
        pass
    
class child (parent):

    def d1(self):

        print("d2 method of abs")
    def d2(self):

        print("d2 method of abs")

    def d3(self):

        print("d2 method of abs")


c=child()
c.d1()
c.d2()
c.d3()