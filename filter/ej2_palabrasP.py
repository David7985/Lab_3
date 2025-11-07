palabras = ["perro","gato","pato","hamster"]
empiezan_p = list(filter(lambda p: p.startswith("p"), palabras))
print(empiezan_p)