"""
Sistema de Arquivos e Navegação

Para fazer uso de manipulação de arquivos do sistema operacional, precisamos importar
e fazer uso do módulo os.

os -> Operating System - Sistema Operacional

# Fazer o import
import os

# getcwd() -> pega o current work directory - diretório de trabalho corrente
# Retorna o path (caminho) absoluto

print(os.getcwd()) # C:/Users/LuizSantos/OneDrive\Curso Paitoun

# Para mudar o diretório, podemos utilizar o chdir()

os.chdir('..')

print(os.getcwd()) # C:/Users/LuizSantos/OneDrive

os.chdir('..')

print(os.getcwd()) # C:/Users/LuizSantos

os.chdir('..')

print(os.getcwd()) # C:/Users

os.chdir('..')

print(os.getcwd()) # C:

# Podemos checar se um diretório é absoluto ou relativo

print(os.path.isabs('C:/Users/')) # True

# OBS para usuários Windows
# Se você, infelizmente, estiver utilizando um computador com Windows,
# terá que ter cuidado ao verificar diretórios.

print(os.path.isabs('C:\\Users'))

# Podemos identificar o sistema operacional com o módulo os
print(os.name) # Posix (Linux e Mac), nt (Windows)

# No windows
import sys

print(os.getcwd()) # C:\\Users\\LuizSantos\\OneDrive\\Curso Paitoun

res = os.path.join(os.getcwd(), 'Aula', 'geek')

os.chdir(res)

print(os.getcwd()) # C:\\Users\\LuizSantos\\OneDrive\\Curso Paitoun\\Aula\\geek

# Veja que o os.path.join() recebe dois parâmetros, sendo o primeiro o diretório atual e o segundo
# o diretório que será juntado ao atual
print(sys.platform)

# Podemos listar os arquivos e diretórios com o listdir()

print(os.listdir('C:\\'))

"""

import os

# Podemos listar os arquivos e diretórios com mais detalhes com scandir()

scanner = os.scandir('C:\\')

arquivos = list(scanner)
print(dir(arquivos[0]))

print(arquivos[0].inode()) # ??
print(arquivos[0].is_dir()) # É um diretório? True
print(arquivos[0].is_file()) # É um arquivo? False
print(arquivos[0].is_symlink()) # É um link simbólico? False
print(arquivos[0].path) # Caminho até o arquivo
print(arquivos[0].stat()) # ???
print(arquivos[0].name) # Nome do arquivo

# OBS: Quando utilizamos a função scandir() nós precisamos fechá-la, assim como quando abrirmos um arquivo

scanner.close()