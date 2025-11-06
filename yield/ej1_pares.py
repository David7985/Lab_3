def generar_pares():
    for n in range(0, 20, 2):
        yield n

for num in generar_pares():
    print(num)