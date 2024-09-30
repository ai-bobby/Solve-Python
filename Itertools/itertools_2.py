import itertools
import operator

list1=[('ali',89),('ahmad',45),('reza',81),('mehdi',98),('mohammad',73),('hamid',49)]
list2=sorted(list1,key=operator.itemgetter(1),reverse=True)
list3=operator.itemgetter(0,1,2,3)(list2)
list4=[item[0] for item in list3]
list5=list(itertools.combinations(list4,3))
list6=list(itertools.permutations(list4,3))

print(list2)
print(list3)
print(list4)
print(len(list5))
print(len(list6))
