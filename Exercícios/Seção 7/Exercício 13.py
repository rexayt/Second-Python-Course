# Fazer um programa para ler 5 valores e, em seguida, mostrar a posição onde se encontram o maior e o menor valor.
lista = []
for c in range(1,6):
    n = int(input('Digite um número: '))
    lista.append(n)
print(f"O maior número é {max(lista)} e se encontra na posição {lista.index(max(lista))}, o menor número é {min(lista)} e se encontra na posição {lista.index(min(lista))}")