#### P(X<1000) =?
import numpy as np
import scipy.stats as state
import math


whights = [1022,1003,998,1006,1012,989]
mean = np.mean(whights)
variance = np.var(whights)
std_deviation = math.sqrt(variance)

print(f"mean : {mean}")
print(f"variance : {variance}")
print(f"std_deviation : {std_deviation}")


dw = 1000
porb = state.norm.cdf(dw , loc=mean,scale=std_deviation)
print(F"P(X<({dw} : {porb:4f}))")

#### P(998<X<1015) =? ....
whights = [1022,1003,998,1006,1012,989]
mean = np.mean(whights)
variance = np.var(whights)
std_deviation = math.sqrt(variance)

print(f"mean : {mean}")
print(f"variance : {variance}")
print(f"std_deviation : {std_deviation}")

lowe_bound = 998
upper_bound = 1015
prob_lower_bound = state.norm.cdf(lowe_bound,loc=mean,scale=std_deviation)
prob_upper_bound = state.norm.cdf(upper_bound,loc=mean,scale=std_deviation)
prob = prob_upper_bound - prob_lower_bound
print(f"P({lowe_bound} <X< {upper_bound}) : {prob}")