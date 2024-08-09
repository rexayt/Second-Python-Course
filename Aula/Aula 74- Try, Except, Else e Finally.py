"""
Try / Except / Else / Finally

Dica de quando e onde tratar código:

TODA ENTRADA DEVE SER TRATADA!

OBS: A função do usuário é DESTRUIR seu sistema.

try:
    num = int(input('Informe um número: '))
except ValueError:
    print('Valor incorreto')
else:
    print(f'Você digitou {num}')

# Finally

try: 
    num = int(input('Informe um número: '))
except ValueError:
    print('Você não digitou um valor válido')
else:
    print(f'Você digitou o número {num}')
finally:
    print('Executando o finally')

# OBS: O bloco finally é SEMPRE executado. Idependente se houve exceção ou não.

# O finally, geralmente, é utilizado para fechar ou desalocar recursos.

# Exemplo mais complexo

def dividir(a, b):
    return a / b

num1 = int(input('Informe o primeiro número: '))

try:
    num2 = int(input('Informe o segundo número: '))
except:
    print('O valor precisa ser numérico')

try:
    print(dividir(num1, num2))
except NameError:
    print('Valor incorreto')

# Exemplo mais complexo

def dividir(a, b):
    return a / b

num1 = int(input('Informe o primeiro número: '))

try:
    num2 = int(input('Informe o segundo número: '))
except:
    print('O valor precisa ser numérico')

try:
    print(dividir(num1, num2))
except NameError:
    print('Valor incorreto')

# Exemplo mais complexo CORRETO
# OBS: Você é responsável pelas entradas das suas funções. Então, trate-as!

def dividir(a,b):
    try:
        return int(a) / int(b)
    except ValueError:
        return 'Valor incorreto'
    except TypeError:
        return 'Digite dois números'
    except ZeroDivisionError:
        return 'Impossível dividir por zero'

num1 = input('Informe o primeiro número: ')
num2 = input('Informe o segundo número: ')

print(dividir(num1, num2))

# Exemplo mais complexo - Genérico
# OBS: Você é responsável pelas entradas das suas funções. Então, trate-as!

def dividir(a,b):
    try:
        return int(a) / int(b)
    except:
        return 'Ocorreu um erro'

num1 = input('Informe o primeiro número: ')
num2 = input('Informe o segundo número: ')

print(dividir(num1, num2))

"""

# Exemplo mais complexo - Semi Genérico
# OBS: Você é responsável pelas entradas das suas funções. Então, trate-as!

def dividir(a,b):
    try:
        return int(a) / int(b)
    except (ValueError, ZeroDivisionError) as err:
        return f'Ocorreu um problema: {err}'

num1 = input('Informe o primeiro número: ')
num2 = input('Informe o segundo número: ')

print(dividir(num1, num2))
