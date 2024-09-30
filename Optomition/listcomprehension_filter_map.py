lst = [1,2,3,4,5,6]

squares = list()

for i in lst:
    squares.append(i**2)
print(squares)


squares = [i ** 2 for i in lst]
print(squares)
squares = list(map(lambda x : x ** 2, lst))
print(squares)

squares = [i ** 2 for i in lst if i % 2 != 0]
print(squares)
squares_map_filter = list(map(lambda x : x**2,filter(lambda x : x % 2 != 0,lst)))
print(squares_map_filter)
squares_dict = dict(map(lambda x : (x , x**2) ,filter(lambda x : x % 2 != 0,lst)))
print(squares_dict)