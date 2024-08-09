"""
Manipulando Data e Hora

Python tem um módulo built-in (integrado) para se trabalhar com data e hora
chamado datetime

import datetime

# print(dir(datetime))

print(datetime.MAXYEAR)

print(datetime.MINYEAR)

print(datetime.datetime.now())  # 2023-04-17 16:28:52.661645 BR 17/12/2018

print(repr(datetime.datetime.now()))

inicio = datetime.datetime.now()

print(inicio)

inicio = inicio.replace(year=2023, hour=16, minute=0, second=0, microsecond=0)

print(inicio)

# Recebendo dados do usuário e convertendo para data

import datetime

evento = datetime.datetime(2019, 1 ,1 ,0)

print(type(evento))

print(type('31/12/2018'))

print(evento)

nascimento = input('Informe sua data de nascimento: ')


nascimento = nascimento.split('/')

nascimento = datetime.datetime(int(nascimento[2]), int(nascimento[1]), int(nascimento[0]))

print(nascimento)

 
print(type(nascimento))

"""

import datetime

evento = datetime.datetime.now()

# Acesso individual dos elementos de data e hora

print(evento.year) # Ano
print(evento.month) # Mês
print(evento.day) # Dia
print(evento.hour) # Hora
print(evento.minute) # Minuto
print(evento.second) # Segundo
print(evento.microsecond) # Microsegundo