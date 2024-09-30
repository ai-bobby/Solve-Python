# فرض کنیم بک سکه دارم و به طور متوسط 30 % رمات شیر می اید
import scipy.stats as stats

p = 0.3
prob_success = stats.bernoulli.pmf(1,p)
print(prob_success)
prob_failure = stats.bernoulli.pmf(0,p)
print(prob_failure)


# -----------------------------------------------------------
# بک سیستم اتوماتیک برای تشخیص ایمیل های اسپم و معمولی داریم احتمال اینکه ایمیل های وارد شده اسپم نباشه 0.9%است
import scipy.stats as stats

p = 0.9
prob_success = stats.bernoulli.pmf(1,p)
print(prob_success)
prob_failure = stats.bernoulli.pmf(0,p)
print(prob_failure)

