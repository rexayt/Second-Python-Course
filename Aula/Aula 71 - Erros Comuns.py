"""
Erros mais comuns em Python

É importante prestar atenção e aprender a ler as saídas de erros geradas pela execução do nosso código.

Os erros mais comuns:

SyntaxError -> Ocorre quando o Python encontra um erro de sintaxe. Ou seja, você escreveu algo que o Python não reconhece como parte da línguagem.

Exemplos SyntaxError

a)
def funcao:
    print('Geek University')

b)
None = 1

2 - NameError -> Ocorre quando uma variável ou função não foi definida.

Exemplos NameError

a)
print(geek)

b)
geek()

3 - TypeError -> Ocorre quando uma função/operação/ação é aplicada a um tipo errado.

Exemplos TypeError

a)
print(len(5))

b)
print('Geet' + [])

4 - IndexError -> Ocorre quando tentamos acessar um elemento em uma lista ou outro tipo de dado indexado utilizando um índice inválido.

Exemplos IndexError

a)
lista = ['Geek']
print(lista[2])

b)
lista = ['Geek']
print(lista[0][10])

5 - ValueError -> ocorre quando uma função/operação built-in (integrada) recebe um argumento com tipo correto mas vaor inapropriado.

Exemplos ValueErro

a)
print(int('Geek'))

6 - KeyError -> Ocorre quando tentamos acessar um dicionário com uma chave que não existe.

Exemplos KeyError

a)
dic = {}
print(dic['geek'])


7 - AttributeError -> Ocorre quando uma variável não tem um atributo/função.

a)
tupla = (1,2 ,3 ,4)
print(tupla.sort())

8 - IdentationError -> Ocorre quando não respeitamos a indentação do Python (4 espaços).

Exemplos IndentationError

a)
def nova():
print("Geek")

OBS: Exceptions e Erros são sinônimos na programação.

OBS: Importante ler e prestar atenção na saída de erro.
"""

