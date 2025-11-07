contador = iter(range(10, 16))
while True:
    try:
        print(next(contador))
    except StopIteration:
        break