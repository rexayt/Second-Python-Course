"""
Sorted

OBS: Não confunda, apesar do nome, com a função sort() 
que já estudamos em Listas. o sort() só funciona em listas

Podemos utilizar o sorted() com qualquer iterável.

Como o próprio nome diz, sorted() serve para ordenar.

OBS: O sorted, sempre retorna uma Lista com os elementos do iterável ordenados

# Exemplo

numeros = [6, 1, 8, 2]
print(numeros)

print(sorted(numeros))      # Ordena do menor para o maior

numeros = [6, 1, 8, 2]

# Adicionando parâmetros ao sorted()

print(sorted(numeros, reverse=True))        # Ordena do maior para o menor

usuarios = [
    {"username": 'samuel','tweets': ["Eu adoro bolos!", 'Eu adoro pizzas']},
    {"username": 'carla','tweets': ["Trabalhei muito hoje..."]},
    {"username": 'joão','tweets': ["Hoje foi muito bom, fui no teatro...", 'Zerei Far Cry 3']},
    {"username": 'jeff','tweets': []},
    {"username": 'pablo','tweets': ["Amanhã eu vou no parque", 'Fui no parque hoje...']},
    {"username": 'caligula','tweets': ["Comi um Méqui hoje, nossa...", 'Hoje eu aprendi a fazer hambúrguer']}
]

# Ordenando por username - Ordem Alfabética
print(sorted(usuarios, key=lambda usuario: usuario['username']))

# Ordenando pelo número de tweets
print(sorted(usuarios, key=lambda usuario: usuario['tweets']))
"""

# Último exemplo

musicas = [
    {'titulo': 'Thunderstruck', 'tocou': 3},
    {'titulo': 'Dead Skin Mask', 'tocou': 2},
    {'titulo': 'Back in Black', 'tocou':4},
    {'titulo': 'Too old to rockn roll, too young to die', 'tocou':32}
]

# Ordena da menos tocada para a mais tocada
print(sorted(musicas, key=lambda musica: musica['tocou']))

# Ordena da mais tocada para a menos tocada
print(sorted(musicas, key=lambda musica: musica['tocou'], reverse=True))