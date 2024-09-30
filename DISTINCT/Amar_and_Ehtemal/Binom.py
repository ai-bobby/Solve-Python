import scipy.stats as stats
import math

##
# 1
n = 7
p = 0.8

x=4
prob = stats.binom.pmf(x,n,p)
print(f"P(X=4) : {prob:.4f}")
print(50 * '-')


# 2
x_values = [6 , 7]
sum_prob = 0
for x in x_values:
    sum_prob += stats.binom.pmf(x,n,p)

print(f"P(X>5) : {sum_prob:.4f}")


# -----------------------------------------------------------------
## 
n = 12
p = 0.75
x_values = [10, 11 ,12]

sum_prob = 0
for x in x_values:
    sum_prob += stats.binom.pmf(x,n,p)

print(f"P(X>=10) : {sum_prob:.4f}")



excepted_value = stats.binom.mean(n,p)
print(f"E(X) : {excepted_value:.2f}")

variance = stats.binom.var(n ,p)
print(f"Var(X) : {variance:.2f}")

std_dev = math.sqrt(variance)
print(f"S.D : {std_dev:.2f}")

cv = (std_dev / (excepted_value)) * 100
print(f"C.V : {cv:.2f}")


