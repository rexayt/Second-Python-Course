lista = [1,2,3,-4,-5,-7,6,2,7]
for c in lista:
    if c < 0:
        i = lista.index(c)
        lista.remove(c)
        lista.insert(i, 0)
print(lista)