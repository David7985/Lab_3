from functools import reduce

num = [7, 3, 9, 1, 5]
mayor = reduce(lambda a, b: a if a > b else b, num)
print(mayor)