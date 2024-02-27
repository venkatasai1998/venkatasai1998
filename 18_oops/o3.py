class product:

    productid=100     #class/static variables
    productname="samsung"

    #instance method
    def getdata(self):

        print(self.productid,self.productname)

    @classmethod
    def productdetails(cls):

        #cls.classvar
        print(cls.productid,cls.productname)

    @staticmethod

    def productdata():
        #classname.class var

        print(product.productid,product.productname)

product().getdata()
product().productdetails()
product.productdata()

#object reference
P=product()
P.productdata()  # we call static method/var only using class name , but not using object reference its not right way to call.