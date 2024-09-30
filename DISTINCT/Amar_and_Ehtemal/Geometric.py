import scipy.stats as stats

p = 0.2
x = 3

prob = stats.geom.pmf(x,p)
print(f"P(X={x} : {prob:.4f})")


# ----------------------------------------------------------    

p = 0.95
x = 5

prob = stats.geom.pmf(x ,p)
print(f"P(X={x} : {prob:.7f})")

