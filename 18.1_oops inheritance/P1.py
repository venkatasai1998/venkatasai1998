# single level
# multilevel inheritance
# multiple level
# hybrid 
# hierarchial inheritance


# single level

# class parent:

#     def d1(self):

#         print("instance method d1")

# class child(parent):

#     def d2(self):

#         print("instance method d2")

# c=child()
# c.d2()
# c.d1()


# multilevel

# class grandparent:

#     def d1(self):
#         print("instance method d1")

# class parent(grandparent):

#     def d2(self):

#         print("instance method d2")

# class child(parent):

#     def d3(self):

#         print("instance method d3")

# c=child()
# c.d1()
# c.d2()
# c.d3()


# multiple
# class grandparent:

#     def d1(self):
#         print("instance method d1")
        
# class parent:

#     def d2(self):

#         print("instance method d2")

# class child(grandparent , parent):

#     def d3(self):

#         print("instance method d3")

# c=child()
# c.d1()
# c.d2()
# c.d3()

# P=parent()
# P.d2()

# g=grandparent()
# g.d1()


#Hierarchial 
class grandparent:

    def d1(self):
        print("instance method d1")
        
class parent(grandparent):

    def d2(self):

        print("instance method d2")

class child_y(grandparent):

    def d3(self):

        print("instance method d3")

class child_o(grandparent):

    def d4(self):

        print("instance method d4")

P=parent()
P.d1()
P.d2()

c=child_y()
c.d1()
c.d3()

c1=child_o()
c1.d1()
c1.d4()