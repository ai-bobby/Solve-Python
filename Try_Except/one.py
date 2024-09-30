# def myIsDigit(x):
#     try:
#         int(x)
#         return True
#     except:
#         return False


# x=input("Enter Number : ")
# if myIsDigit(x):
#     x=int(x)
#     print(x/10)
# else:
#     print("Error")
#---------------------------------------------------------------------------

# def emailValidator(email):
#     if email[0].isdigit():
#         raise RuntimeError("Email start by number...")
#     elif '@' not in email:
#         raise RuntimeError("Email Format invalid...")
#     elif 'yahoo.com' not in email and 'gmail.com' not in email:
#         raise RuntimeError("Server is invalid...")
#     return email


# def mobileValidator(mobile):
#     if not mobile.isdigit() or len(mobile)!=11 or mobile[:2]!='09':
#         raise RuntimeError("Mobile format invalid...")
#     return mobile


# email=input("Please enter email : ")
# mobileNumber=input("Please enter MobileNumber : ")
# try:
#     emailValidator(email)
#     print(f"Email : {email}")
#     mobileValidator(mobileNumber)
#     print(f"Mobile : {mobileNumber}")
# except RuntimeError as error:
    # print(error)

# -----------------------------------------------------------------------------------
# class MyException1(Exception):
#     def __init__(self,message):
#         super().__init__(message="MyException1")
#         self.message = message

#     def __str__(self):
#         return self.message
# #--------------------------------------------------------
# class MyException2(Exception):
#     def __init__(self,message):
#         super().__init__(message="MyException1")
#         code=1
#         self.message = message+" "+code

# #--------------------------------------------------------
# class MyException3(Exception):
#     pass
# #--------------------------------------------------------

# class Student:
#     def fun1():
#         pass
    
#     def dataTypeValidte(dataType1):
#         if dataType1==0:
#             obj1=MyException1("sakjdgjsgjhsgdcugsa")
#             raise obj1
        
        
        
        
        
       
        
