"""
Trabalhando com Módulos Builtin (módulos integrados, que já vem instalados no Python)
________________________
|Python|Módulos builtin|
------------------------


import random as rdm
#import random

print(rdm.random())

# Importando todo o módulo

import random

print(random.random())


# Utilizando alias (apelidos) para módulos/funções

from random import randint as rdi, random as rdm

print(rdi(5,89))

print(rdm)
"""
# Costumamos a utilizar tuple para colocar múltiplos imports de um mesmo módulo
from random import (random, randint, shuffle, choice)

print(random)

print(randint(3,7))

lista = ['Geek', 'University', 'Python']
shuffle(lista)
print(lista)

print(choice('University'))