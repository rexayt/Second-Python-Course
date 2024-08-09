"""
Módulos Externos

Utilizamos o gerenciador de pacotes Python chamado Pip - Python Installer Package

Você pode conhecer todos os pacotes externos oficiais em: https://pypi.org

colorama -> É utilizado para permitir impressão de textos coloridos no terminal.

from geek import geek1, geek2

from geek.university import geek3, geek4

print(geek1.pi)

print(geek1.funcao1(4, 6))

print(geek2.funcao2())

print(geek3.funcao3())

print(geek4.funcao4())
"""

from geek.geek1 import funcao1

print(funcao1(6, 9))
from geek.university.geek4 import funcao4

print(funcao4())