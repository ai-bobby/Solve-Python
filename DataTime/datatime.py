# import datetime
# import khayyam

# # d1 = datetime.date.today()
# # print(d1)

# # jd1=khayyam.JalaliDate(d1)
# # print(jd1)

# # d2=jd1.todate()
# # print(d2)

# def dec1(func):
#     def inner(*args):
#        print(f'{func(*args)}') 
#        dt=khayyam.JalaliDatetime(datetime.datetime.today()).strftime('%Y/%m/%d %H:%M:%S')
#        print(f'DateTime : {dt}')
#     return inner


# @dec1
# def variz(message):
#     return message

# @dec1
# def bardasht(message):
#     return message


# variz("Mablagh 2000000 riyal variz shode.")
# bardasht("sdflsa hdfks ahfsjba fkshafis adhfisaud")