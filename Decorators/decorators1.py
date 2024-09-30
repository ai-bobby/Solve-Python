def append_sum_list(func):
    def inner(numList):
        numList.append(sum(numList))
        return numList
    return inner


@append_sum_list
def printList(list1):
    return list1


list1=[12.34,13,13.45,19.75,13.45,16.5]
print(printList(list1))