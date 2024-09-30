import itertools
import operator

list1=[
    {'name':'Fizik','score':14.5,'value':3},
    {'name':'Riyazi','score':11.25,'value':4},
    {'name':'Dini','score':17.75,'value':2},
]

list2=[dic['score']*dic['value']  for dic in list1]

print(list2)
print(list(itertools.accumulate(list2,operator.add)))

