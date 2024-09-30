# from struct import pack

# def pack1(**kwargs):
#     print(kwargs)

# def unpack2(name,age,job):
#     print(name)
#     pack1(Name=name,Age=age,Job=job)

# def unpack1(person1,person2,person3):
#     unpack2(*person1)
#     unpack2(*person2)
#     unpack2(*person3)



# list1=[
#     ("Ali",18,"Teacher"),
#     ("Mehdi",43,"Employee"),
#     ("Reza",37,"Manager"),
#     ]
# unpack1(*list1)



def fun1(*args):
    sum=0
    for item in args:
        sum+=item
    print(sum)

fun1(23,45)
fun1(23,45,435,65,7,658)
fun1(23,45,435,65)
fun1()