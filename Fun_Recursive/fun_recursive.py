# for i in range(10):
#     for j in range(10):
#         for k in range(10):
#             for h in range(10):
#                 print(i,end="")
#                 print(j,end="")
#                 print(k,end="")
#                 print(h)

# -------------------------------------------------------------------------
def incNumber(str1):                 # '0000'
    list1=[int(ch) for ch in str1]   # [0,1,0,1]
    j=len(list1)-1                   # j=1
    while True:
        if list1[j]+1<10:
            break
        list1[j]=0
        j-=1
    list1[j]+=1
    list1=[str(item) for item in list1]
    return ''.join(list1)
    

def printNumber(str1):
    if(str1!='0444'):
        print(str1)
        str1=incNumber(str1)            
        printNumber(str1)

printNumber('0000')
# ------------------------------------------------------------------------
def incNumber(str1):                 # '0000'
    list1=[ord(ch) for ch in str1]   # [97,97,97,97]
    j=len(list1)-1                   # j=3
    while True:
        if list1[j]+1<ord('z')+1:
            break
        list1[j]=ord('a')
        j-=1
    list1[j]+=1
    list1=[chr(item) for item in list1]
    return ''.join(list1)
    

def printNumber(str1):
    if(str1!='accc'):
        print(str1)
        str1=incNumber(str1)            
        printNumber(str1)

printNumber('aaaa')