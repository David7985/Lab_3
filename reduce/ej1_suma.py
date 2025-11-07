from functools import reduce

num = [5, 10, 15, 20]
sum = reduce(lambda a, b: a + b, num)
print(sum)