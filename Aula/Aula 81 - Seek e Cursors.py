"""
Seek e Cursor

seek() -> É utilizada para movimentar o cursos pelo arquivo.

arquivo = open('Aula/texto.txt', encoding='utf-8')

print(arquivo.read())

# seek() -> A função seek() é utilizada para movimentação do cursor pelo arquivo. Ela recebe um
# parâmetro que indica onde queremos colocar o cursosr.
 
# Movimentando o cursor pelo arquivo com a função seek(). -> Procurar

arquivo.seek(21)

print()
print(arquivo.read())

# readline() -> Função que lê o arquivo linha a linha (readline -> lê linha)

ret = arquivo.readline()

print(type(ret))

print(ret)

print(ret.split(' '))

# readlines() -> Função que lê todas as linhas

linhas = arquivo.readlines()

print(len(linhas))

# OBS: Quando abrimos um arquivo com a função open() é criada uma conexão entre o arquivo
no disco do computador e o nosso programa. Essa conexão é chamada de streaming. Ao finalizar
os trabalhos com o arquivo devemos fechar essa conexão. Para isso utilizamos a função close()

Passos para se trabalhar com um arquivo:

1 - Abrir o arquivo;

2 - Trabalhar o arquivo;

3 - Fecha o arquivo;

# 1 - Abrir o arquivo;
arquivo = open('Aula/texto.txt', encoding='utf-8')

# 2 - Trabalhar o arquivo;
print(arquivo.read())

print(arquivo.closed) # False - verifica se o arquivo está aberto ou fechado

# 3 - Fecha o arquivo;
arquivo.close()

print(arquivo.closed) # True - verifica se o arquivo está aberto ou fechado

print(arquivo.read())

# OBS: Se tentarmos manipular o arquivo após seu fechamento, teremos um ValueError

"""

arquivo = open('Aula/texto.txt', encoding='utf-8')

# Com a função read() podemos limitar a quantidade de caracteres a serem lidos no arquivo
print(arquivo.read(50))

