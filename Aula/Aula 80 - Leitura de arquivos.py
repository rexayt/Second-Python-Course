"""
Leitura de Arquivos

Para o conteúdo de um arquivo em Python, utilizamos a função integrada open(),
que literalmente significa 'abrir'.

open() -> Na forma mais simples de utilização nós passamos apenas um parâmetro
de entrada, que neste caso é o caminho do arquivo a ser lido. Essa função retorna
um _io.TextIOWrapper e é com ele que trabalhamos então.

https://docs.python.org/3/library/functions.html#open

# OBS: Por padrão, a função open() abre o arquivo para a leitura. Este arquivo
deve existir, ou então teremos o erro FileNotFoundError

mode r -> Modo de leitura. r -> read() -> ler

"""

# Exemplo

arquivo = open('Aula/texto.txt', encoding='utf-8')

# print(arquivo)

# print(type(arquivo))

# Pra ler o conteúdo de um arquivo, após a sua abertura, devemos utilizar a função read()

ret = arquivo.read()

print(type(ret))
print(ret)

# print(arquivo.read())

# OBS: O Python, utiliza um recurso para trabalhar com arquivos chamado cursor. Esse cursor,
# funciona como o cursor quando estamos escrevendo.

# OBS: A função read() lê todo o conteúdo do arquivo