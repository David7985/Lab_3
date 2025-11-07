class Impares:
    def __iter__(self):
        for n in range(1, 21, 2):
            yield n

for num in Impares():
    print(num)