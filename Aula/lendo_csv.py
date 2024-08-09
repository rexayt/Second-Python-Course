"""
Lendo arquivos CSV

CSV - Comma Separated Values - Valores Separados por Vírgula

# Separador por vírgula

1, 2, 3, 4, 5, 6

"geek", "university", "python", "ciência", "dados"

# Separador ponto e vírgula

1; 2; 3; 4; 5; 6

"geek"; "university"; "python"; "ciência"; "dados"

# Separador por espaço

1 2 3 4 5 6

"geek" "university" "python" "ciência" "dados"

# Possível de se trabalhar, mas não é o ideal (trabalhoso)

with open(r'.\lutadores.csv', encoding='utf8') as arquivo:
    dados = arquivo.read()
    print(type(dados))
    dados = dados.split(',')[3:]
    print(dados)

A linguagem Python possui duas formas diferentes para ler dados em arquivos CSV:
    - reader -> Permite que iteremos sobre as linhas do arquivo CSV como listas;
    - DictReader -> Permite que iteremos sobre as linhas do arquivo CSV como OrderedDicts;

# Reader

from csv import reader

with open(r'.\lutadores.csv', encoding='utf8') as arquivo:
    leitors_csv = reader(arquivo)
    print(type(leitors_csv))
    next(leitors_csv)   # Pular o cabeçalho
    for linha in leitors_csv:
        # Cada linha é uma lista
        print(f'{linha[0]} nasceu em {linha[1]} e mede {linha[2]} centímetros')    

# DictReader

from csv import DictReader

with open(r'.\lutadores.csv', encoding='utf8') as arquivo:
    dictReader = DictReader(arquivo)
    for linha in dictReader:
        # Cada linha é um OrderedDict
        print(f'{linha["Nome"]}, nasceu no país {linha["País"]} e mede {linha["Altura (em cm)"]}')


"""

# DictReader

from csv import DictReader

with open(r'.\lutadores.csv', encoding='utf8') as arquivo:
    dictReader = DictReader(arquivo, delimiter=',')
    for linha in dictReader:
        # Cada linha é um OrderedDict
        print(f'{linha["Nome"]}, nasceu no país {linha["País"]} e mede {linha["Altura (em cm)"]}')