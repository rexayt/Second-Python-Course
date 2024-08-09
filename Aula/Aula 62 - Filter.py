"""
Filter

filter() -> Serve para filtrar dados de uma determinada coleção.

# Biblioteca para trabalhar com dados estatísticos
import statistics

# Dados coletados de algum sensor
dados = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]

# Calculando a média dos dados utilizando a função mean()
media = round(statistics.mean(dados))

# OBS: Assim como a função map(), a filter() recebe dois parâmetros, sendo uma 
# função e um iterável

res = filter(lambda valor: valor > media, dados)
print(list(res))

# OBS: Assim como na função map(), após serem utilizados os dados de filter() eles serão excluídos da memória.

paises = ['', 'Argentina', '', 'Brasil', 'Chile', '', 'Colombia', '', 'Equador', '', '', 'Venezuela']

print(paises)

res = filter(None, paises)

print(list(res))

paises = ['', 'Argentina', '', 'Brasil', 'Chile', '', 'Colombia', '', 'Equador', '', '', 'Venezuela']

res = filter(lambda pais: len(pais.strip()) > 0, paises)

print(list(res)) 


# A diferença entre map() e filte() é:

# map() -> Recebe dois parâmetros, uma função e um iterável e retorna um objeto
# mapeando a função para cada elemento do iterável

# filter() -> Recebe dois parâmetros, uma função e um iterável e retorna um objeto filtrando apenas os elementos de acordo com a função


# Exempo mais complexo

usuarios = [
    {"username": 'samuel','tweets': ["Eu adoro bolos!", 'Eu adoro pizzas']},
    {"username": 'carla','tweets': ["Trabalhei muito hoje..."]},
    {"username": 'joão','tweets': ["Hoje foi muito bom, fui no teatro...", 'Zerei Far Cry 3']},
    {"username": 'jeff','tweets': []},
    {"username": 'pablo','tweets': ["Amanhã eu vou no parque", 'Fui no parque hoje...']},
    {"username": 'caligula','tweets': ["Comi um Méqui hoje, nossa...", 'Hoje eu aprendi a fazer hambúrguer']}
]

# Filtrar os usuários que estão inativos no Twitter

# Forma 1
# inativos = list(filter(lambda x: len(x['tweets']) == 0, usuarios))

# Forma 2
inativos = list(filter(lambda x: not x['tweets'], usuarios))

print(inativos)
"""

# Combnar filter() e map()

nomes = ['Vanessa', 'Ana', 'Maria']

# Devemos criar uma lista contendo 'Sua instrutora é' + nome, desde que cada nome tenha menos de 5 caracteres

lista = list(map(lambda nome: f'Sua instrutora é {nome}', filter(lambda nome: len(nome) < 5, nomes)))

print(lista)