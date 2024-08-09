"""

Conjuntos

- Conjuntos em qualquer línguagem de programação, estamos fazendo referência à Teoria dos Conjuntos da matemática

- Aqui no Python, os conjuntos são chamaos de Sets

Dito isso, da mesma forma que na matemática

- Sets (conjuntos) não possuem valores duplicados;
- Sets (conjuntos) não possuem valores ordenados;
- Elementos não são acessados via índice, ou seja, conjuntos não são indexados;

Conjuntos são bons para se utilizar quando precisamos armazenar elementos mas não nos importamos com a ordenação deles. Quando não precisamos
nos preocupar com chaves, valores e itens duplicados.

Os conjuntos (sets) são referenciados em Python com chaves {}

# Definindo um conjunto:

# Forma 1

s = set({1, 2, 3, 4, 5, 5, 6, 7, 2, 3}) # Repare que temos valores repetidos

print(s)
print(type(s))

# OBS: Ao criar um conjunto, caso seja adicionado um valor já existente, o mesmo será ignorado sem gerar error e não fará parte do conjunto

# Forma 2 - Mais comum

s = {1, 2, 3, 4, 5, 5}
print(s)
print(type(s))

# Podemos verificar se determinado elemento está contido no conjunto

if 3 in s:
    print("Tem o 3")
else:
    print("Não tem o 3")

# Importante lembrar que, além de não termos valores duplicados, não temos ordem

#Lista aceitam valores duplicados, então temos 10 elementos
dados = '99', '2', '34', '23', '12', '1', '44', '5'

lista = list(dados)
print(f'Lista: {lista}')

# Tupla aceitam valores duplicados, então temos 10 elementos
tupla = tuple(dados)
print(f"Tupla = {tupla}")

# Dicionários não aceitam chaves duplicadas, então temos 8 elementos
dicionario = {'dicionário': dados}
print(f'Dicionário: {dicionario}')

# Listas aceitam valores duplicados, então temos 8 elementos   
conjunto = {dados}
print(f'Conjunto: {conjunto}')

# Assim como todo outro conjunto Python podemos colocar tipos de dados misturados em Sets

s = {1, 'b', True, 34.22, 44}
print(s)
print(type(s))

# Podemos iterar em um set normalmente
for valor in s:
    print(valor)

# Usos interessantes com sets

# Imagine que fizemos um formulário de cadastro de visitantes em uma feira ou museu e os visitantes informam manualmente a cidade de onde vieram

# Nós adicionamos cada cidade em uma lista Python, já que em uma lista podemos adicionar novos elementos e ter repetição.

cidades = ['Belo Horizonte', 'São Paulo', 'Campo Grande', 'Cuiaba', 'Campo Grande', 'São Paulo', 'Cuiaba']

# Agora precisamos saber quantas cidades distintas, ou seja, únicas, temos.

# O que você faria? Faria um loop na lista....?

# Podemos utilizar o set pra isso:

print(len(set(cidades)))

# Adicionando elementos em um conjunto
s = {1,2,3}

s.add(4)
s.add(4) # Duplicidade não gera erro. Simplesmente é ignorado e não adicionado.
print(s)

# Remover elementos em um conjunto.
s = {1,2,3}

print(s)

# Forma 1

s.remove(3) #Não é índice! Informamos o valor a ser removido.

print(s)

# OBS: Caso o valor não seja encontrado será gerado o erro KeyError, Nenhum valor é retornado.

# Forma 2

s.discard(22)

print(s)

# OBS: Se o valor não for encontrado, nenhum erro é gerado.

# Copiando um conjunto para outro...

# Forma 1 - Deep Copy

novo = s.copy()
print(novo)

novo.add(4)

print(novo)
print(s)

# Forma 2 - Shallow Copy

novo = s

novo.add(4)

print(novo)
print(s)

# Podemos remover todos os itens de um conjunto

s.clear()

# Métodos Matemáticos de Conjuntos

# Imagine que temos dois conjuntos: Um contendo estudantes do curso Python e um contendo estudantes do curso de Java
# Precisamos gerar um conjunto com nomes de estudantes únicos.

# Forma 1 - Utilizando union

print(estudantes_java.union(estudantes_python))

# Forma 2 - Utilizando o caractere pipe |

print(estudantes_python | estudantes_java)

# Gerar um conjunto de estudantes que estão em ambos os cursos.

# Forma 1 - Utilizando intersection

print(estudantes_java.intersection(estudantes_python))

# Forma 2 - Utilizando o &
print(estudantes_python & estudantes_java)



estudantes_python = {'Marcos', 'Patrícia', 'Ellen', 'Pedro', 'Julia', 'Guilherme'}
estudantes_java = {'Fernando', 'Gustavo', 'Julia', 'Ana', 'Patrícia'}

# Veja que alguns alunos que estudam Python também estudam Java.

# Gerar um conjunto de estudantes que não estão no outro curso

print(estudantes_java.difference(estudantes_python))
print(estudantes_python.difference(estudantes_java))

"""
# Soma*, Valor Máximo*, Valor Mínimo, Tamanho

# * Se os valores forem todos inteiros ou reais

s = {1, 2, 3, 4, 5, 6}

print(sum(s))
print(max(s))
print(min(s))
print(len(s))
