"""
Sistema de arquivos - manipulação

# Descobrindo se um arquivo ou diretório existe
print(os.path.exists('arquivo.txt')) # False
print(os.path.exists('frutas.txt')) # True

# Diretório

# Paths relativos
print(os.path.exists('Aula\\geek')) # True
print(os.path.exists('Aula\\geek\\university')) # True
print(os.path.exists('Aula\\geek\\university\\geek3.py')) # True
print(os.path.exists('outro')) # False

# Paths absolutos
print(os.path.exists('C:\\Users\\LuizSantos\\OneDrive\\Curso Paitoun\\Aula\\geek\\university'))

# Criando arquivos

# Forma 1
open('arquivo-teste.txt', 'w').close()

# Forma 2
open('arquivo-teste.txt', 'a').close()

# Forma 3

with open('arquivo-teste.txt', 'w') as arquivo:
    pass

# Criando arquivos
os.mknod('')

# OBS: Se você estiver utilizando no Mac OS, pode haver um erro de PermissionError

# OBS: Criando um arquivo via mknod() se o arquivo já existir teremos o erro FileExistsError

Path Relativo
os.mkdir('templates')

# OBS: A função mkdir() cria um diretório se este não existir. Caso exista, teremos FileExistsError

os.mkdir('C:\\Users\\LuizSantos\\OneDrive\\Curso Paitoun\\Aula\\templates')

# OBS: Se não tivermos permissão para criar o diretório teremos um PermissionError

# Criando multi-diretórios (árvore de diretórios)
os.mkdir('templates/geek/university/outro')

# OBS: Se já existir. Teremos um FileExistsError

os.makedirs('templates2/novo2/outro2', exist_ok=True)

# Diretórios
os.rename('geek2/olá/publico', 'geek2')

# OBS: Se o diretório não existir teremos um FileNotFoundError

# OBS: Se o diretório que queremos renomear não estiver vazio. teremos um OSError

# Arquivos
os.rename('geek2/olá/publico/teste.txt', 'geek2/olá/publico/geek.txt')

# Renomear arquivos e diretórios
os.rename('frutas.txt', 'cesta.txt')

# ATENÇÃO! Tome cuidado com os comandos de deleção. Ao deletarmos um arquivo ou diretório, eles
# não vão para a lixeira. Eles somem.

# Removendo arquivos
os.remove('geek')

# OBS: Se você estiver no Windows e o arquivo que você for deletar estiver em uso,

# OBS: Caso o arquivo não exista, teremos o FileNotFoundError

# OBS: Se você informar um diretório ao invés de um arquivo, teremos um IsADirectoryError

# Removendo diretório vazios

os.rmdir('geek2')

# OBS: Se o diretório tiver qualquer conteúdo teremos um OSError

# Removendo uma árvore de diretórios

for arquivo in os.scandir('geek'):
    if arquivo.is_file():
        os.remove(arquivo.path)

# Podemos remover uma árvore de diretórios vazios

os.removedirs('geek2/mais')

# Se algum dos diretórios contiver arquivos ou outros diretórios, o processo para.
        
os.remove('cesta1.txt') # Não vai para a lixeira. É deletado imediatamente

# ATENÇÃO: Ao remover arquivos e diretórios com Python eles não vão para a lixeira. Eles vão embora!

# Importando a biblioteca send2trash (Envia arquivos e diretórios para a lixeira)
from send2trash import send2trash

send2trash('cesta2.txt') # Vai para a lixeira. Pode ser restaurado

# OBS: Se o arquivo não existir, teremos OSError

# Trabalhando com arquivos e diretórios temporários

import os
import tempfile

with tempfile.TemporaryDirectory() as tmp:
    print(f'Criei o diretório temporário em {tmp}')
    with open(os.path.join(tmp, 'arquivo_temporario.txt'), 'w') as arquivo:
        arquivo.write('Geek university\n')
    input()

# Estamos criando um diretório temporário, abrindo o mesmo e dentro dele criando
# um arquivo para escrevermos um texto. No final, usamos um input() só para mantermos
    # os arquivos temporários 'vivos' dentro dos blocos with.

# OBS: possivelmente, o código acima não irá funcionar se você estiver utilizando
# o Windows (funcionou no meu rsrs). Por conta desse sistema trabalhar de forma diferente com arquivos
# temporários

# Criando um diretório temporário

with tempfile.TemporaryFile() as tmpfile:
    tmpfile.write(b"Geek University\n")
    tmpfile.seek(0)
    print(tmpfile.read())

# OBS: Em arquivos temporários só conseguimos escrever bits. Por isso, utilizamos b'<string>'

https://docs.python.org/3/library/os.html?highlight=os#module-os
"""


