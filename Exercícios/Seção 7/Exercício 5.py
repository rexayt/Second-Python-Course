# Leia um vetor de 10 posições. Contar e escrever quantos valores pares ele possuí.
lista = [1,2,3,4,5,6,7,8,9,10]
par = 0
for n in lista:
    if n % 2 ==0:
        par += 1
print(f"A lista tem {par} valores pares")