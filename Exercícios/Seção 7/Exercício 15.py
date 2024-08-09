# Leia um vetor com 20 números inteiros. Escreva os elementos do vetor eliminando elementos repetidos
s = set({})
for c in range(10):
    n = int(input("Digite um número: "))
    s.add(n)
print(f'Os números repetidos foram {s}')