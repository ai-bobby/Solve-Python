import numpy as np 

rand_numbers = np.random.uniform(low=0,high=1,size=5)
print(rand_numbers)


rand_numbers = np.random.uniform(size=5)
print(rand_numbers)



rand_numbers = np.random.uniform(10,20,5)
print(rand_numbers)


np.random.seed(0)
rand_numbers = np.random.uniform(low=0,high=1,size=5)
print(rand_numbers)



# ----------------------------------------------------------------
import numpy as np 
import matplotlib.pyplot as plt

def uniform_probability_density(x,a,b):
    if x < a or x > b:
        return 0
    else:
        return 1 / (b - a)
    

a = 2
b = 8
mean = (a + b) / 2
variance = ((b - a) ** 2) / 12
print(f"E(x) : {mean}")
print(f"Var(x) : {variance}")



# P(3<x<5)
c = 3
d = 5
probability_x_lt_p = (d - c) / (b - a)
print(f'P({c} <= x =< {d}) : {probability_x_lt_p}')



# P(x<6)
c = a
d = 6
probability_x_lt_p = (d - c) / (b - a)
print(f'P({c} <= x =< {d}) : {probability_x_lt_p}')

# P(3<x)
c = 3
d = b
probability_x_lt_p = (d - c) / (b - a)
print(f'P({c} <= x =< {d}) : {probability_x_lt_p}')


x_values = np.linspace(a - 1,b + 1,100)
prob_values = [uniform_probability_density(x,a,b) for x in x_values]
plt.plot(x_values,prob_values)
plt.xlabel('x')
plt.ylabel('Y')
plt.show()