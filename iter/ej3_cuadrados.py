class CuadradosLista:
    def generar_lista(self):
        return [n ** 2 for n in range(1, 11)]

print(CuadradosLista().generar_lista())