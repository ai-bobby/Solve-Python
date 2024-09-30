# ### Iterator
# import random
# pisctures=['a.jpg','b.jpg','c.jpg','d.jpg','e.jpg','f.jpg','g.jpg','h.jpg']

# def fun1(pisctures):
#     return random.choice(pisctures)

# for p1 in iter(lambda:fun1(pisctures),'e.jpg'):
#     print(p1)

# ----------------------------------------------------------------------------------------------------
def fun():
  fact = 1
  value = None
  while True:
    value = yield fact
    fact *= value

  
g1 = fun()
next(g1)
for i in range(1,10):
  print(i,g1.send(i))