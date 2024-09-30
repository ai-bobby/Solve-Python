words=('abcba','aabaa','sddffs','alkla','eoppppoq','wmdmwolo','wwwlllwww')
print(list(filter(lambda word: word!=word[::-1],words)))



# -------------------------------------------------
# products=[
#     {'name':'A','price':10000,'brand':'LG'},
#     {'name':'B','price':10000,'brand':'SONY'},
#     {'name':'C','price':10000,'brand':'SNOVA'},
#     {'name':'D','price':10000,'brand':'SONY'},
# ]

# brand=input("Enter Brand : ")
# print(list(filter(lambda product : product['brand']==brand,products)))


