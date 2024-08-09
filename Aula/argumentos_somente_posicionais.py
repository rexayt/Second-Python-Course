"""
Argumentos Somente Posicionais
"""

# valor = "67.3"
# print(float(valor))

# def cumprimenta_v1(nome):
#     return f'Olá {nome}'

# print(cumprimenta_v1('Geek'))
# print(cumprimenta_v1(nome='Geek'))

# def cumprimenta_v2(nome, /):
#     return f'Olá {nome}'

# print(cumprimenta_v2('Geek'))
# print(cumprimenta_v2(nome='Geek'))

def cumprimenta_v3(nome, /, mensagem='Olá'):
    return f'Olá {nome} {mensagem}'

print(cumprimenta_v3('Geek'))
print(cumprimenta_v3('University', mensagem='Hello'))
print(cumprimenta_v3('Felicity', 'Bem-vinda'))