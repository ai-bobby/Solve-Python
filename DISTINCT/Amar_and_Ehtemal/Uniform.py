import numpy as np
from scipy.stats import randint
import matplotlib.pyplot as plt

a , b = 10 , 20
x_value = np.r_[a:b+1]          # x_value = np.linspace(a,b+1,11)
uniform_pmf = randint.pmf(x_value, a,b+1)
print(x_value , '\n' ,uniform_pmf)

x = 18
index = np.where(x_value==x)[0][0]
print(f"P(X={x} : {uniform_pmf[index]:.4f})")



# -----------------------------------------------------------

sum_prob = 0
for x in range(a,13):
    index = np.where(x_value==x)[0][0]
    sum_prob += uniform_pmf[index]

print(f"P(X={x} : {sum_prob:.4f})")

plt.plot(x_value, uniform_pmf,'bo', ms=10)
plt.vlines(x_value,0,uniform_pmf,color='r',lw=1,alpha=0.2)
plt.xlabel("X_value")
plt.ylabel("Probability")
plt.show()