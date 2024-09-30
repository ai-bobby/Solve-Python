# d = {'a' : 4 , 'b' : 9 , 'c' : 7 , 'd' : 8 , 'e' : 0 , 'f' : 4}
# sorted_value = sorted(d.values())
# print(sorted_value)
# sorted_d = dict()

# # 1
# for i in sorted_value:
#     for k in d.keys():
#         if d[k] == i:
#             sorted_d[k]=d[k]




# ## 2
# sorted_d = {k:v for k,v in sorted(d.items(),key= lambda x :x[1])}

# ## 3
# sorted_d = {k : d[k] for k in sorted(d,key=d.get)}

# ## 4
# from operator import itemgetter
# sorted_d = {k:v for k,v in sorted(d.items(),key = itemgetter(1))}


# ## 5
# from operator import itemgetter
# sorted_d = dict(sorted(d.items(),key = itemgetter(1)))

# print(sorted_d)


# ---------------------------------------------------------------------------------------
from operator import itemgetter
d = {'a' : 4 , 'b' : 9 , 'c' : 7 , 'd' : 8 , 'e' : 0 , 'f' : 4}
soreted_d = dict(sorted(d.items(),key=itemgetter(1)))
print(soreted_d)



