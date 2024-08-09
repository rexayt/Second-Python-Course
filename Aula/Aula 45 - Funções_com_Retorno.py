"""
Funções com retorno
numeros = [1, 2, 3]

ret = numeros.pop()

print(f'Retorno de pop: {ret}')

print(numeros)

OBS: Em Python, quando uma função não retorna nenhum valor, o retorno é None

OBS: Funções Python que retornam valores, devem retornar estes valores com a palavra reservada return

OBS: Não precisamos necessariamente criar uma variável para receber o retorno de uma função. Podemos passar a execução da função para outras funções.

# Vamos refatorar esta função para que ela retorne o valor
def quadrado_de_7():
    return 7*7

# Criamos uma variável para receber o retorno da função.
ret = quadrado_de_7()
print(f"Retorno {ret}")

print(f"Retorno: {quadrado_de_7()}")

def diz_oi():
    return 'Oi!'

print(diz_oi())

OBS: Sobre a palavra reservada return

1 - Ela finaliza a função, ou seja, ela sai da execução da função;
2 - Podemos ter, em uma função, diferentes returns;
3 - Podemos, em uma função, retornar qualquer tipo de dado e até mesmo múltiplos valores;

# Exemplo 1 - Ela finaliza a função, ou seja, ela sai da execução da função

def diz_oi():
    return 'Oi! '
    print('Estou sendo executado após o retorno...')

print(diz_oi())

# Exemplo 2 - Podemos ter, em uma função, diferentes returns

def nova_funcao(var):
    variavel= var
    if variavel:
        return 4
    elif variavel is None:
        return 3.2
    return 'b'
print(nova_funcao(True))

# Exemplo 3 - Podemos, em uma função, retornar qualquer tipo de dado e até mesmo múltiplos valores

def outra_funcao():
    return 2, 3, 4, 5

num1, num2, num3, num4 = outra_funcao()
print(num1,num2,num3)

# Vamos criar uma função para jogar a moeda

from random import randint

def joga_moeda():
    # Gera um númerlo pseudo-randômico entre 0 e 1
    valor = randint(0,1)
    if valor == 0:
        return 'Cara'
    return 'Coroa'

print(joga_moeda())

# Erros comuns na utilização do retorno, que na verdade nem é erro, mas sim codificação desnecessária.

def eh_impar():
    numero = 5
    if numero % 2 != 0:
        return True
    else:
        return False
    
print(eh_impar())
"""

