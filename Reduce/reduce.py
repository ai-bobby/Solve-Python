from functools import reduce
list1=[23,45,200,232,65,3,6557,156,80]

print(reduce(lambda a,b: a if a<b else b,list1))
print(reduce(lambda a,b: a if a>b else b,list1))



list2=[1,1,2,3,5,8,13,21,34]
print(reduce(lambda a,b: a + b ,list2))
