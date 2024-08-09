"""
Módulo Collections - Named Tuple

https://docs.python.org/3/library/collections.html#collections.OrderedDict

# Recap tupla
tupla = (1, 2, 3)

print(tupla[1])

Named Tuple -> São tuplas, diferenciadas, onde, específicamos oum nome para a mesma e também parâmetros.

"""

# Importando

from collections import namedtuple

# Precisamos definir o nome de parâmetros.

# Forma 1 - Declaração Named Tuple

cachorro = namedtuple('cachorro', 'idade raca nome')

# Forma 2 - Declaração Named Tuple

cachorro = namedtuple('cachorro', 'idade, raca, nome')

# Forma 3 - Declaração Named Tuple 
cachorro = namedtuple('cachorro', ['idade', 'raca', 'nome'])

# Usando

ray = cachorro(idade=2, raca='Chow-Chow', nome='Ray')

# Acessando os dados

# Forma 1

print(ray[0])
print(ray[1])
print(ray[2])

# Forma 2

print('Idade: ',ray.idade) # Idade
print('Raça: ',ray.raca) # Raca
print('Nome: ',ray.nome) # Nome