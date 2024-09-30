from scipy.stats import expon


prob = expon.cdf(x=1,scale=0.25)
print('Probability :',1-prob)
# ---------------------------------------------------------
prob = expon.cdf(x=10,scale=5)
print('Probability :',1-prob)
# ---------------------------------------------------------
prob = expon.cdf(x=1,scale=2)
print('Probability :',1-prob)
# ---------------------------------------------------------
prob = expon.cdf(x=5,scale=2)
print('Probability :',1-prob)