import numpy as np
import matplotlib.pyplot as plt



data_list = [
                5000,5000,5500,5800,6000,6500,
                8000,8000,8000,8500,9000,9500,
                10000,10500,10500,10500,11000,12000,
                16000,16000,16500,17000,17500,18000,
                20000,21000,22000,22000,23000,43000
            ]

# print(data_list)



data_array = np.array(data_list)
# print(data_array)



data_array_2d = data_array.reshape(5,6)
# print(data_array_2d)



mean_of_year = np.mean(data_array_2d,axis = 1)
print(mean_of_year)



mean_of_month_year = np.mean(data_array_2d,axis = 0)
print(mean_of_month_year)



max_year = np.amax(data_array_2d)
row,col = np.where(data_array_2d==max_year)
# print(f"year {row[0]+1} month {col[0]+1}")



new_value = data_array_2d[4,]
orginal_value = data_array_2d[0,]
# print(orginal_value)
# print(new_value)

sub_value = np.subtract(new_value,orginal_value)
div_value = np.divide(sub_value,orginal_value)
percent_change_value = div_value * 100
# print(percent_change_value)



x = np.array(['1396','1397','1398','1399','1400'])
y=mean_of_year
plt.plot(x,y)
plt.show()

x = np.array(['1','2','3','4','5','6'])
data_list_split = np.split(data_array_2d,5)
index = 1
print(data_list_split)
for y in data_list_split:
    plt.subplot(3,2,index)
    plt.plot(x,y.flatten())
    index +=1



x = np.array(['1396','1397','1398','1399','1400'])
plt.subplot(3,2,6)
plt.plot(x,mean_of_year)
plt.show()