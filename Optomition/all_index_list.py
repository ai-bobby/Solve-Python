scores = [10,20,16,19,18,17]

is_acsepted = True

for score in scores:
    if score < 10 :
        is_acsepted = False
        break


print(is_acsepted)
print(all(score >= 10 for score in scores))