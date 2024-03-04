#encapsulation is a techniques that binds or wrapping the data and corresponding methods into a single unit
#encapsulation provides datahiding and data protection
#data protection through access specifier
#1) private : only inside the class and class methods 
#2) protector: inside class and its intermediate subclass
#3) public : entire program

#public
# class test:
#     def result(self):

#         self.id=101

# t=test()
# t.result()
# print(t.id)

#protector
# class test:
#     def _result(self):

#         self._id=101

# t=test()
# t._result()
# print(t._id)


#private
# class test:
#     def result(self):

#         self.__id=101
#         print(self.__id)

# t=test()
# t.result()
#private method
# class user:
#     def __init__(self):

#         self.__id=101
#         self.__name="sai kiran"

#     def result(self):
#         print(self.__id,self.__name)

# u=user()
# u.result()

#private using mangling

# class user:
#     def __init__(self):

#         self.__id=101
#         self.__username="sai kiran"


# u=user()
# print(u._user__id)
# print(u._user__username)


# setters and getters 

class student:

    def setdetails(self,sid,sname):

        self.__id=sid      #private variables
        self.__name=sname

    def getdetails(self):

        print(self.__id,self.__name)

s=student()
s.setdetails(101,"sai kiran")
s.getdetails()
