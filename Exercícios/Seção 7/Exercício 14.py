# Faça um programa que leia um vetor de 10 posições e verifique se existem valores iguais e os escreva na tela
lista = []
repetido = []
for c in range(10):
    n = int(input("Digite um número: "))
    if n in lista:
        repetido.append(n)
    repetido.sort()
    lista.append(n)
print(f'Os números repetidos foram {repetido}')