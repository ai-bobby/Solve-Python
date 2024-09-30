import collections
list1=[
    {'name':'ali','age':30},
    {'name':'reza','age':25},
    {'name':'mehdi','age':18},
    {'name':'mohammad','age':25},
    {'name':'mehdi','age':18},
    {'name':'ahmad','age':25},
]

list2=[dic['age'] for dic in list1]
print(list2)

print(collections.Counter(list2).most_common(2))

# ----------------------------------------------------------------
import collections 
Person=collections.namedtuple('Person','Name Avg Age')
p1=Person('Ali',14.56,18)
p2=Person('Mehdi',18.25,24)
p3=Person('Reza',12.30,19)
p4=Person('Ahmad',19.78,48)
list1=[p1,p2,p3,p4]
print(list1)

list2=[item for item in list1 if item.Avg>15]
print(list2)


# ---------------------------------------------------------------------
import collections

class MyList(collections.UserList):
    def append(self,x):
        if x in self:
            print("Error: %s" % x)
        else:
            collections.UserList.append(self,x)
        
    
    
    

list1=MyList([12,34,56,89,90])
list1.append(34)
print(list1)