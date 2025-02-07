"""
Min e Max

max() -> Retorna o maior valor em um iterável ou o maior de dois ou mais elemento.

# Exemplos

lista = [1, 8, 4, 99, 34, 129]
print(max(lista))       # 129

tupla = (1, 8, 4, 99, 34, 129)
print(max(tupla))       # 129

conjunto = {1, 8, 4, 99, 34, 129}
print(max(conjunto)) # 129

dicionario = {'a': 1, 'b': 8, 'c': 4, 'd': 99, 'e': 34, 'f': 129}
print(max(dicionario)) # f

# Faça um programa que receba dois valores do usuário e mostre o maior
val1 = int(input('Digite um número: '))
val2 = int(input('Digite um número: '))

print(max(val1,val2))

print(max(4, 67, 54))

print(max('a', 'ab', 'abc'))

print(max('a', 'b', 'c', 'g'))

print(min(3.145, 5.789))

print(min('Geek University'))

# Outros exemplos

nomes = ['Arya', 'Samson', 'Dora', 'Tim', 'Ollivander']

print(max(nomes))

print(min(nomes))

print(max(nomes, key=lambda nome: len(nome)))       # Ollivander

print(min(nomes, key=lambda nome: len(nome)))       # Tim
"""

musicas = [
    {'titulo': 'Thunderstruck', 'tocou': 3},
    {'titulo': 'Dead Skin Mask', 'tocou': 2},
    {'titulo': 'Back in Black', 'tocou':4},
    {'titulo': 'Too old to rock`n roll, too young to die', 'tocou':32}
]

print(max(musicas, key=lambda musica: musica['tocou']))
print(min(musicas, key=lambda musica: musica['tocou']))

# DESAFIO! Imprima somente o título da música mais e menos tocada
print(max(musicas, key=lambda musica: musica['tocou'])['titulo'])
print(min(musicas, key=lambda musica: musica['tocou'])['titulo'])

# DESAFIO! Como encontrar a música mais tocada e a menos tocada sem usar max(), min() e lambda?
me = 1000
ma = 0
menor = maior = ''
for musica in musicas:
    if me > musica['tocou']:
        menor = musica['titulo']
    elif ma < musica['tocou']:
        maior = musica['titulo']
print(maior)
print(menor)