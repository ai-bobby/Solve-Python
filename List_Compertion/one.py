# list_one=[1,2,3,4,5,6]
# list_duplicate=[item for item in list_one]
# print(list_duplicate)


# str_one="gfdsjgkd gdhsjgklfdsh   ghdsjklgh ds  hsdkgh ds   dhskglhd"
# delete_str=''.join([ch for ch in str_one if ch !=" "])
# print(delete_str)


# str_one="gfdsjgkd gdhsjgklfdsh nnnnnnnnaff  ghdsjklgh ds  hsdkgh ds   dhskglhd"
# word_delete=['a','b','m','n']
# delete_str=''.join([ch for ch in str_one if ch not in word_delete])
# print(delete_str)


# str_one="gfdsjgkd gdhsjgklfdsh ghdsjklgh ds hsdkgh ds dhskglhd"
# delete_str=''.join(["\t" if ch ==' ' else ch for ch in str_one])
# print(delete_str)

# ----------------------------------------------------------------------------------------------------

# list1=[10,20,30,40,50,60]
# list2=[item for item in list1 if item%3==0]
# print(list2)


# str1="mehdi ali      reza ahmad mohammad    sara"
# str2=''.join([ch for ch in str1 if ch!=' '])
# print(str2)


# str1=input("Enter Text : ")
# removeList=['m','e','a',' ']
# print(''.join([ch for ch in str1 if ch not in removeList]))



# str1="mehdi ali reza ahmad mohammad sara"
# str2=''.join(['\t' if ch==' ' else ch for ch in str1])
# print(str2)
# -------------------------------------------------------------------------------------------------
# def printMatrix(matrix):
#    print('\n'.join(['\t'.join([f'{col}' for col in row]) for row in matrix])) 


# matrix1=[
# 	[23,56,78],
# 	[10,20,30],
# 	[9,34,17],
# 	[5,30,67]
# ]

# matrix2=[[col+(0.1*col) if col>20 else col for col in row] for row in matrix1]


# printMatrix(matrix1)
# print(100*'-')
# printMatrix(matrix2)


# ---------------------------------------------------------------------------------
# names=['sara','tara','ali','mahsa','tatha','reza','mohammad']
# print([name for name in names if name[-1]=='a'])

# list1=[10,3,120,8,20,30,45,8,10,40,50,60]
# list2=sorted(list1)
# print(list1)
# print(list2)