"""
Escrevendo em arquivos CSV

reader (leitor), writer (escritor)

writerow() -> Escreve uma linha

# writer() -> Gera um objeto para que possamos escrever em um arquivo CSV. Utilizamos o método
# writerow() -> para escrever cada linha. Este métod recebe uma lista.


from csv import writer

with open('filmes.csv', 'w+', encoding='utf8') as arquivo:
    escritor_csv = writer(arquivo)
    escritor_csv.writerow(['Título', 'Gênero', 'Duração'])
    while True:
        filme = input('Informe o nome do filme: ')
        if filme.lower() in 'sair':
            break
        genero = input('Informe o gênero: ')
        duracao = input('Informe a duração (em minutos): ')
        escritor_csv.writerow([filme, genero, duracao])

        



"""

# DictWriter

# OBS: As chaves do dicionário devem ser as mesmas utilizadas como cabeçalho.

from csv import DictWriter

with open('filmes3.csv', 'a+', encoding='utf8') as arquivo:
    escritor_csv = DictWriter(arquivo, fieldnames=['Título', 'Gênero', 'Duração'])
    escritor_csv.writeheader()
    while True:
        filme = input('Informe o nome do filme: ')
        if filme.lower() in 'sair':
            break
        genero = input('Informe o gênero: ')
        duracao = input('Informe a duração (em minutos): ')
        escritor_csv.writerow({"Título": filme, 'Gênero': genero, "Duração": duracao})