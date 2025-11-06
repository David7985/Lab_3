class Cuadrados:
    def __iter__(self):
        for n in range(1, 11):
            yield n ** 2

for cu in Cuadrados():
    print(cu)