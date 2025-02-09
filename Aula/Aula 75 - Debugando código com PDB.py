"""
Debuggando com PDB

PDB -> Python Debugger

Vida de Inseto -> Life's Bug

Bug -> Inseto

# OBS: A utilização do print para debugar código é uma prática ruim.

def dividir(a,b):
    try:
        return int(a) / int(b)
    except (ValueError, ZeroDivisionError) as err:
        return f'Ocorreu um problema: {err}'

# Existem formmas mais profissionais de se fazer esse 'debug', utilizando o debugger
# Em Python, podemos fazer isso em diferentes IDEs, como o PyCharm ou utilizando o debugger
# o PDB - Python Debugger

# Exemplo com o PyCharm

def dividir(a,b):
    try:
        return int(a) / int(b)
    except (ValueError, ZeroDivisionError) as err:
        return f'Ocorreu um problema: {err}'
    
print(dividir(4, 7))

# Exemplo com PDB - Python Debugger - Exemplo 1

# Para utilizar o Python Debugger, precisamos* importar a biblioteca pdb
# e então utilizar a função set_trace()

# Comandos básicos do PDB
# l (listar on estamos no código)
# p (imprime variável)
# c (continua a execução - finaliza o debugging)
import pdb

nome = 'Angelina'
sobrenome = 'Jolie'
pdb.set_trace()
nome_completo = nome + ' '+ sobrenome
curso = 'Programação em Python: Essencial'
final = nome_completo + ' faz o curso ' + curso
print(final)

# Exemplo com PDB - Python Debugger - Exemplo 2

# Para utilizar o Python Debugger, precisamos* importar a biblioteca pdb
# e então utilizar a função set_trace()

# Comandos básicos do PDB
# l (listar on estamos no código)
# p (imprime variável)
# c (continua a execução - finaliza o debugging)

nome = 'Angelina'
sobrenome = 'Jolie'
import pdb; pdb.set_trace()
nome_completo = nome + ' '+ sobrenome
curso = 'Programação em Python: Essencial'
final = nome_completo + ' faz o curso ' + curso
print(final)

# Por que utilizar este formato?
# O debug é utilizado durante o desenvolvimento. Costumamos realizar todos
# imports de bibliotecas no ínicio do arquivo. Por isso, ao invés de colocarmos
# o import do pdb no início do arquivo, nós colocamos somente onde vamos
# debuggar, e ao finalizar já fazemos a remoção.

# Exemplo com PDB - Python Debugger - Exemplo 2

# Para utilizar o Python Debugger, precisamos* importar a biblioteca pdb
# e então utilizar a função set_trace()

# * No Python 3.7, não é mais necessário importar a biblioteca pdb,
# pois o comando de debug foi incorporado como função bultin (integrada)
# chamada breakpoin

# Comandos básicos do PDB
# l (listar on estamos no código)
# p (imprime variável)
# c (continua a execução - finaliza o debugging)

nome = 'Angelina'
sobrenome = 'Jolie'
breakpoint()
nome_completo = nome + ' '+ sobrenome
curso = 'Programação em Python: Essencial'
final = nome_completo + ' faz o curso ' + curso
print(final)


"""

# OBS: Cuidado com os conflitos entre nomes de variáveis e os comandos do pdb

def soma(l, n, p, c):
    breakpoint()
    return l + n + p + c


print(soma(1, 2, 3, 4))

# Como os nomes das variáveis são os mesmos dos comandos do pdb, devemos
# utilizar o comando p para imprimir as variáveis. Ou seja: p variável 