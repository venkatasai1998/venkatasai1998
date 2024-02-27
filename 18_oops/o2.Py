# oops
#instance var ,class or static var

# class product:

# # instance method
#     def displayproducts(self,productid,productname,productprice):
#         self.pid=productid # instancev
#         self.pname=productname
#         self.pprice=productprice
#         print(self.pid,self.pname,self.pprice)

# P=product()
# P.displayproducts("101","samsung",1000)


# class employees:

# # instance method
#     def getemployees(self,employeeid,employeename):
#         self.eid=employeeid # instancev
#         self.ename=employeename

#     def display(self):
        
#         print(self.eid,self.ename)

# e=employees()
# e.getemployees("12934","saikiran")
# e.display()


class product:

# instance method
    def displayproducts(self,productid,productname,productprice):
        self.pid=productid # instancev
        self.pname=productname
        self.pprice=productprice
        print(self.pid,self.pname,self.pprice)

P=product()
P.displayproducts("101","samsung",1000)
delattr("productid")
