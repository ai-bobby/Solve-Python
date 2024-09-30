### saving and showing customer contact information
# ====================================================================================================
#-------------------------------------- classes and subclasses ---------------------------------------
## parent class
class Address:
    def __init__(self, number, street, city):
      self.number = number
      self.street = street
      self.city = city
      self.address = {}
      
    # creating a dictionary for address attributes
    def add_Address_Attribute(self):
      self.address["No"] = self.number
      self.address["Street"] = self.street
      self.address["City"] = self.city
      return self.address

    # method overriding occurs  
    def show_Info(self):
        print(f"No.{self.number}\t{self.street}\t{self.city}") 
# -----------------------------------------------------
## parent class
class Person:
    def __init__(self, id, name, family, mobile, email):
      self.id = str(id)
      self.name = name
      self.family = family
      self.mobile = mobile
      self.email = email
      self.person = {}

    # creating a dictionary for person's attributes
    def add_Person_Attribute(self):
      self.person["ID"] = self.id
      self.person["Name"] = self.name
      self.person["Family"] = self.family
      self.person["Mobile"] = self.mobile
      self.person["Email"] = self.email
      return self.person
        
    # overriding
    def show_Info(self):
        print(self.id + " " + self.name + " " + self.family + " " + self.mobile + " " + self.email) 
# -----------------------------------------------------
## child class
class Contact(Person,Address):
    def __init__(self, id,name, family, mobile, email, number, street, city):
      Person.__init__(self,id, name, family, mobile, email)
      Address.__init__(self,number, street, city)
      self.contact = {}
    
    # creating a dictionary of contact
    def add_Person_Address(self):
        dic1 = self.add_Person_Attribute() 
        dic2 = self.add_Address_Attribute()
        for dic in (dic1,dic2):
          self.contact.update(dic)
        return self.contact       

    # overriding
    def show_Info(self):
        Person.show_Info(self)
        Address.show_Info(self)
# -----------------------------------------------------
class Phone_Book:
    def __init__(self):
      self.contacts = []      
    
    # creating a list of dictionary for phone book
    def add_Contact(self,contact_Dic):
        self.contacts.append(contact_Dic)
        return self.contacts        

    def show_Info(self):
      for contact in self.contacts:
          for value in contact.values():
            print(value, end=" ")
          print()            
    
    # search customer by family
    def search_Customer(self,family):
      tempList = []
      for contact in self.contacts:
        if family == contact["Family"]:
          tempList.append(contact)
          
      if tempList == []:
        print("Unknown Customer")
      else:
        for contact in tempList:
          contact = Contact(contact["ID"], contact["Name"], contact["Family"], contact["Mobile"], contact["Email"], contact["No"], contact["Street"], contact["City"])
          contact.show_Info()           
# ====================================================================================================
#---------------------------------------- main program -----------------------------------------------
contact1 = Contact(1,"Sara","Amini","09123453423","s@yahoo.com","23","sadi","karaj")
contact_Dic1 = contact1.add_Person_Address()

contact2 = Contact(2,"Bahar","Karami","09122345678","b@yahoo.com","44","razi","tehran")
contact_Dic2 = contact2.add_Person_Address()

contact3 = Contact(3,"Sima","Amini","091363785645","sima@yahoo.ca","20","bahar","tehran")
contact_Dic3 = contact3.add_Person_Address()

phonebook = Phone_Book()
phonebook.add_Contact(contact_Dic1)
phonebook.add_Contact(contact_Dic2)
phonebook.add_Contact(contact_Dic3)
phonebook.show_Info()

print("********************")


family = input("Enter family for search : ")
phonebook.search_Customer(family)
# print("********************")
# phonebook.search_Customer("Rezaee")
# print("********************")
# phonebook.search_Customer("Sarlak")
# # ====================================================================================================
# #------------------------------------------ output ---------------------------------------------------

  




