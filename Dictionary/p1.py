### Dictionary

def getStudentAvg(list_dictionary):
    tempList=[]
    for student in list_dictionary:
        for key,value in student.items():
            avg=sum(value)/len(value)
            tempList.append({key:avg})
    return tempList
    
    

list_dictionary=[
    {"ali":[13,15.5,16,17,12.5]},
    {"mehdi":[15,17,18]},
    {"reza":[19.25,15.4,17]}
    ]

print(getStudentAvg(list_dictionary))