# Faça um programa que preencha um vetor com 10 números reais, calcule e mostre a quantidade de números negativos e a soma dos números positivos desse vetor
lista = []
negativo = 0
for c in range(1,11):
    n = float(input(f"Digite o {c}º número real: "))
    lista.append(n)
    if n < 0:
        negativo += 1
print(f'Existem {negativo} números negativos')