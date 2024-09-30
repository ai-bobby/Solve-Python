names=["mehdi","reza","ali","mohammad","ahmad","sahar"]


list2=[[ch for ch in item if ch!='a'] for item in list(map(list,names))]
print(list2)

# -----------------------------------------------------------------------------
list1 = [10,20,30]
list2 = [10,15,13]
list3 = [18,54,122]

print(list(map(lambda a,b,c : a+b+c ,list1,list2,list3)))
# -----------------------------------------------------------------------------
def fun1(n):
  return n*10

def fun2(n):
  return n+100

def fun3(n):
  return n+500


def map_fun(x,functions):
  list_res = []
  for func in functions:
    list_res.append(func(x))
  return list_res


print(map_fun(5,(fun1,fun2,fun3)))