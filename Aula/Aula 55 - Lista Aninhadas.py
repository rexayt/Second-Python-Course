"""
Listas Aninhadas

- Algumas linguagens de programação (C/Java) possuem uma estrutura de dados chamadas de arrays:
    - Unidimensionais (Arrays / Vetores);
    - Multidimensionais (Matrizes);

Em Python nós temos as Listas

numeros = [1, 'b', 3.234, True, 5]

# Exemplos 

listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] # Matriz 3 x 3

print(listas)

print(type(listas))

# Como fazemos para acessar os dados?

print(listas[0][1]) # 2
print(listas[2][1]) # 8

listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] # Matriz 3 x 3

# Iterando com loops em uma lista aninhada
for lista in listas:
    for num in lista:
        print(num)

# List Comprehension

[[print(valor) for valor in lista] for lista in listas]


from random import randint
tabuleiro = [[randint(0,10) for numero in range(1,4)] for valor in range(1,4)] # Para cada valor em um range de 1 - 4, crie uma lista de 3 números aleatórios de 0, 10
print(tabuleiro)

# Gerando jogadas para o jogo da velha
velha = [['X' if numero % 2 == 0 else 'O' for numero in range(1,4)] for valor in range(1,4)]

# Gerando valor inicial

print([['*' for i in range(1, 4)] for j in range(1, 4)])
"""