class product:
    #instance method
    def getproductdata(self,productid,productname):
        self.pid=productid
        self.pname=productname
        print(self.pid,self.pname)

        print(productid,productname) # we can call parametres without using self keyword
    @classmethod
    def productdata(cls,productid,productname):
         cls.pid=productid                      # we can call using this attribute method
         cls.pname=productname
         print(cls.pid,cls.pname)
        #print(cls.productid,cls.productname)   #AttributeError: type object 'product' has no attribute 'productid'
         print(productid,productname)
    @staticmethod
    def productdetails(productid,productname):
        

        print(productid,productname)
        
        



product().getproductdata(101,"samsung")
product().productdata(102,"sony")
product().productdetails(103,"nokia")
