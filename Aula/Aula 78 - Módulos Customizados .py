"""
Módulos customizados

Como módulos Python nada mais são do que arquivos Python, então TODOS os arquivos que criamos nesse curso, são módulos python, prontos para serem utilizados.

# Importando uma função específica do nosso módulo
from Aula_46_Funcoes_com_Parametros import soma_impares

print(soma_impares([1, 2, 3, 4, 5, 6, 7, 8, 9]))

"""

import Aula_46_Funcoes_com_Parametros

print(Aula_46_Funcoes_com_Parametros.lista)

print(Aula_46_Funcoes_com_Parametros.tupla)

print(Aula_46_Funcoes_com_Parametros.soma_impares(Aula_46_Funcoes_com_Parametros.lista))