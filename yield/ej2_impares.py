def filtrar_impares(lista):
    for n in lista:
        if n % 2 != 0:
            yield n

num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in filtrar_impares(num):
    print(i)