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
import datetime
class Bill:
    def __init__(self,bill_code,customer_code):
        self.bill_code = bill_code
        self.bill_date =str(datetime.datetime.now()) 
        self.customer_code = customer_code
        self.bill_details=[]
        

    def __str__(self):
        return f"{self.bill_code}\t{str(self.bill_date)}\t{self.customer_code}\t"
# ----------------------------------------------------------------------------
import json

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

try:       
    def read_product_from_json_file():
            with Files('Json_Opp\data\products.json','r') as file_json:
                product = json.load(file_json)
            return product
    
    def show_product_list(products):
        for product in products:
            print(product)

    def read_customers_from_json_file():
        with Files("Json_Opp\data\customers.json",'r') as file_json:
            customers=json.load(file_json)
        return customers

    def show_customerList(customers):
        for customer in customers:
            print(customer)
    
except Exception as error:
    print(error)

# -----------------------------------------------------------------
products=read_product_from_json_file()       
show_product_list(products)    
print(80*'-')
customers=read_customers_from_json_file()       
show_customerList(customers)
# -----------------------------------------------------------------
def create_bill(bill_code,customer_code):
    bill1 = Bill(bill_code,customer_code)
    bill_details1 = BillDetails(1,bill_code,1,5)
    bill_details2 = BillDetails(2,bill_code,3,10)
    bill_details3 = BillDetails(3,bill_code,2,4)
    bill1.bill_details = [bill_details1.__dict__,bill_details2.__dict__,bill_details3.__dict__]
    return bill1.__dict__


def read_bill_from_json_file():
    with Files('Json_Opp/data/bills.json','r') as file_json:
        try :
            current_bills = json.load(file_json)
        except :
            current_bills = []

    return current_bills

def write_bill_json_file(bills):
    with Files('Json_Opp/data/bills.json','w') as file_json:
        json.dump(bills,file_json,indent=4)

current_bills = read_bill_from_json_file()
my_bill = create_bill(1,1000)
current_bills.append(my_bill)
my_bill = create_bill(2,1001)
current_bills.append(my_bill)
my_bill = create_bill(3,1002)
current_bills.append(my_bill)
write_bill_json_file(current_bills)