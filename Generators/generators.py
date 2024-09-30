def get_sum_avg():
    sum=0
    counter=0
    while True:
        num=int(input("Enter Number : "))
        if num!=0:
            sum+=num
            counter+=1
            avg=sum/counter
            yield sum
            yield avg
        else:
            break
        
iter1=get_sum_avg()  
for item in iter1:
    print(item)