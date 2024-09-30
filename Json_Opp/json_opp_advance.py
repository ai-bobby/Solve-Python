import json
import datetime


# ----------------------------------------------------------------------------------------
class Files:
    def __init__(self,file_nsme,file_mode):
        self.file_name = file_nsme
        self.file_mode = file_mode
        self.file_content = None

    def __enter__(self):
        self.file_content = open(self.file_name, self.file_mode)
        return self.file_content
    
    def __exit__(self,*exc_value):
        if self.file_content :
            self.file_content.close()

# ----------------------------------------------------------------------------------------
class Base(object):
    @staticmethod
    def readObjectsFromJsonFile(path):
        with Files(path,'r') as file1:
            try:
                currentObjects=json.load(file1)
            except:
                currentObjects=[]
        return currentObjects

    @staticmethod
    def writeObjectsToJsonFile(path,objects):
        with Files(path,'w') as file1:
            json.dump(objects, file1,indent=4)
    
    @classmethod
    def addObjectToJsonFile(cls,path,object):
        object = cls.readObjectsFromJsonFile(path)
        object.append(object)
        cls.writeObjectsToJsonFile(path,object)
# ----------------------------------------------------------------------------------------
class Product:
    def __init__(self,product_code,product_name,price,product_group):
        self.product_code = product_code
        self.product_name = product_name
        self.price = price
        self.product_group = product_group

    
    def __str__(self):
        return f"{self.product_code}\t{self.product_name}\t{self.price}\t{self.product_group}\t"
# ----------------------------------------------------------------------------------------
class Customer:
    def __init__(self,customer_code,name,family,mobile):
        self.customer_code = customer_code
        self.name = name
        self.family = family
        self.mobile = mobile
# -----------------------------------------------------------------
class BillDetails:
    def __init__(self,bill_details_code,bill_code,product_code,product_count):
        self.bill_details_code = bill_details_code
        self.bill_code = bill_code
        self.product_code = product_code
        self.product_count = product_count

    def __str__(self):
        return f"{self.bill_details_code}\t{self.bill_code}\t{self.product_code}\t{self.product_count}\t"

# --------------------------------------------------------------------------
class Bill:
    def __init__(self,bill_code,customer_code):
        self.bill_code = bill_code
        self.bill_date =str(datetime.datetime.now()) 
        self.customer_code = customer_code
        self.bill_details=[]
        
    def addBillDetails(self,billDetails):
        self.bill_details.append(billDetails)

    def __str__(self):
        return f"{self.bill_code}\t{str(self.bill_date)}\t{self.customer_code}\t"
# ----------------------------------------------------------------------------
class Shop(Base):
    def __init__(self,shop_name):
        self.shop_name = shop_name
        self.products=self.__readObjectsFromJsonFile("Json_Opp\data\products.json")
        self.customers=self.__readObjectsFromJsonFile("Json_Opp\data\customers.json")
        self.bills=self.__readObjectsFromJsonFile("Json_Opp/data/bills.json")


    def __readObjectsFromJsonFile(self,path):
        self.object = []
        with Files(path,'r') as file1:
            try:
                return json.load(file1)
            except json.JSONDecodeError:
                return []

    def __show_list(self,title,list):
        print(100*'=')
        print(f"{title}  : \n"+10*"-")
        if len(list) > 0:
            for item in list:
                print(item)
        else:
            print(f"{title} list is empty")      

    def showProductList(self):
        self.__show_list("Product",self.products)


    def showCustomerList(self):
        self.__show_list("Customer",self.customers)

    def showBillList(self):
        self.__show_list("Bill",self.bills)

# ----------------------------------------------------------------------------
def readBillDetail(billDetailCode,billCode):
    productCode=int(input("Enter Product Id :"))
    productCount=int(input("Enter product Count :"))
    return BillDetails(billDetailCode,billCode,productCode,productCount).__dict__


def createBill():
    billCode=int(input("Enter Bill Code :"))
    customerCode=int(input("Enter Customer Code :"))
    bill1=Bill(billCode,customerCode)
    bill1.addBillDetails(readBillDetail(1,billCode))
    return bill1.__dict__ 



shop1=Shop("Bobby")
shop1.showProductList()
shop1.showCustomerList()
shop1.showBillList()


bill_1 = createBill()
print(bill_1)
shop1.addObjectToJsonFile('./Json_Opp/data/bills.json',bill_1)
# ---------------------------------------------------------------
# import json
# import datetime
# #--------------------------------------------------------------------
# class Base(object):
#     @staticmethod
#     def readObjectsFromJsonFile(path):
#         with open(path,'r') as file1:
#             try:
#                 currentObjects=json.load(file1)
#             except:
#                 currentObjects=[]
#         return currentObjects

#     @staticmethod
#     def writeObjectsToJsonFile(path,objects):
#         with open(path,'w') as file1:
#             json.dump(objects, file1,indent=4)
    
#     @classmethod
#     def addObjectToJsonFile(cls,path,object):
#         objects=cls.readObjectsFromJsonFile(path)
#         objects.append(object)
#         cls.writeObjectsToJsonFile(path,objects)
                
# #--------------------------------------------------------------------
            
# class Product(Base):
#     def __init__(self,productCode,productName,price,productGroupName):
#         self.productCode= productCode
#         self.productName= productName
#         self.price= price
#         self.productGroupName=productGroupName
        
#     def __str__(self):
#         return f"{self.productCode}\t{self.productName}\t{self.price}\t{self.productGroupName}\t"
# #--------------------------------------------------------------------
# class Customer(Base):
#     def __init__(self,customerCode,name,family,mobile):
#         self.customerId = customerCode
#         self.name = name
#         self.family = family
#         self.mobileNumber = mobile
        
#     def __str__(self):
#         return f"{self.customerId}\t{self.name}\t{self.family}\t{self.mobileNumber}\t"
# #-------------------------------------------------------------------
# class BillDetails:
#     def __init__(self,billDetailCode,billCode,productCode,productCount):
#         self.billDetailCode = billDetailCode
#         self.billCode = billCode
#         self.productCode = productCode
#         self.productCount = productCount
        
#     def __str__(self):
#         return f"{self.billDetailCode}\t{self.billCode}\t{self.productCode}\t{self.productCount}\t"
# #-------------------------------------------------------------------
# class Bill(Base):
#     def __init__(self,billCode,customerCode):
#         self.billCode = billCode
#         self.billDate =str(datetime.datetime.now()) 
#         self.customerCode = customerCode
#         self.billDetails=[]

#     def addBillDetails(self,billDetails):
#         self.billDetails.append(billDetails)
        
#     def __str__(self):
#         return f"{self.billCode}\t{str(self.billDate)}\t{self.customerCode}\t"
# #------------------------------------------------------------------
# class Shop(Base):
#     def __init__(self,shopName):
#         self.shopName = shopName
#         self.products=self.__readObjectsFromJsonFile("data/products.json")
#         self.customers=self.__readObjectsFromJsonFile("data/customers.json")
#         self.bills=self.__readObjectsFromJsonFile("data/bills.json")
       
#     def __readObjectsFromJsonFile(self,path):
#         self.objects=[]
#         with open(path,'r') as file1:
#             try:
#                 return json.load(file1)
#             except json.JSONDecodeError:
#                 return []
            
   
#     def __showList(self,title,list):
#         print(100*"=")
#         print(f"{title}  : \n"+10*"-")
#         if len(list)>0:
#             for item in list:
#                     print(item)
#         else:
#             print(f"{title} list is empty")        
            
                
#     def showProductList(self):
#         self.__showList("Product",self.products)


#     def showCustomerList(self):
#         self.__showList("Customer",self.customers)

#     def showBillList(self):
#         self.__showList("Bill",self.bills)

# #-------------------------------------------------------------
# def readBillDetail(billDetailCode,billCode):
#     productCode=int(input("Enter Product Id :"))
#     productCount=int(input("Enter product Count :"))
#     return BillDetails(billDetailCode,billCode,productCode,productCount).__dict__

# def createBill():
#     billCode=int(input("Enter Bill Code :"))
#     customerCode=int(input("Enter Customer Code :"))
#     bill1=Bill(billCode,customerCode)
#     bill1.addBillDetails(readBillDetail(1,billCode))
#     return bill1.__dict__    


  
# shop1=Shop("Darsman")
# shop1.showProductList()
# shop1.showCustomerList()
# # shop1.showBillList()




# myBill=createBill() 
# print(myBill)
# shop1.addObjectToJsonFile("data/bills.json",myBill)



