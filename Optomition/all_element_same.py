my_list = [5,5,5,5,5,5,5,5,5,5,5]

def all_element_same(lst):
    if not lst: return True
    firest_elemnt = lst[0]
    for i in lst:
        if firest_elemnt != i: return False
    return True
print(all_element_same(my_list))



def all_element_same1(lst):
    return len(set(lst)) == 1

print(all_element_same1(my_list))



def all_element_same2(lst):
    return True if all(x == lst[0] for x in lst) else False

print(all_element_same2(my_list))



def all_element_same3(lst):
    return True if lst.count(lst[0]) == len(lst) else False


print(all_element_same3(my_list))
