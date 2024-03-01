from abc import ABC,abstractmethod

class parent(ABC):
    

    def d1(self):
        print("d1 non abs method")

    @abstractmethod

    def d2(self):

        pass
    
class child (parent):

    def d2(self):

        print("d2 method of abs")


c=child()
c.d1()
c.d2()