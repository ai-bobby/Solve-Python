import scipy.stats as stats

lambda_ = 2.3
x_value = 0

poisson_prob = stats.poisson.pmf(x_value,mu=lambda_)
print(poisson_prob)


# ----------------------------------------------------------------

lambda_ = 2.3
x_value = [0,1,2,3]

sum_prob = 0
for x in x_value:
    poisson_prob = stats.poisson.pmf(x,mu = lambda_)
    sum_prob += poisson_prob

res = 1 - sum_prob
print(res)