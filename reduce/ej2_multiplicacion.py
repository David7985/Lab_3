from functools import reduce

num = [2, 3, 4]
mul = reduce(lambda a, b: a * b, num)
print(mul)