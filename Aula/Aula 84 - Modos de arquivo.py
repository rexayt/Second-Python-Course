"""
Modos de abertura de arquivo

r -> Abre para leitura - padrão
w -> Abre para escrita - sobrescreve caso o arquivo já exista
x -> Abre para escrita somente se o arquivo não existir. Caso o arquivo exista, gera FileExistsError
a -> Abre para escrita, adicionando o conetúdo ao final do arquivo.
+ -> Abre para o modo de atualização: Leitura e Escrita. (Temos o controle do cursor)

# OBS: Abrindo no modo 'a' -> append, se o arquivo não existir será criado. Caso exista, o novo conteúdo
será adicionado ao final do arquivo SEMPRE. Com o modo 'a', não controlamos o cursor
http://docs.python.org/3/library/functions.html#open

# Exemplo x
try:
    with open('university.txt', 'x', encoding='utf-8') as arquivo:
        arquivo.write('Teste de conteúdo\n')
except FileExistsError:
    print('Arquivo já existe')

with open('frutas.txt', 'a', encoding='utf') as arquivo:
    while True:
        fruta = input('Informe uma fruta ou sair: ')
        if fruta != 'sair':
            arquivo.seek(0)
            arquivo.write(fruta)
            arquivo.write('\n')
        else:
            break

# Exemplo a
with open('outro.txt','a', encoding='utf-8') as arquivo:
    arquivo.seek(0)
    arquivo.write('Olá!\n')
    arquivo.write('Nova linha.\n')
    arquivo.write('Mais uma linha.\n')
 
# Exemplo r+
with open('outro.txt','r+', encoding='utf-8') as arquivo:
    arquivo.write('Adicionada!\n')
    arquivo.seek(11)
    arquivo.write('Nova linha.\n')
    arquivo.seek(12)
    arquivo.write('Mais uma linha.\n')


"""
