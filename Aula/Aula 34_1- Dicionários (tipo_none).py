"""
Tipo None

O tipo de dado None em Python representa o tipo sem tipo, ou poderia ser conhecido também como tipo vazio porém, falar que é um tipo sem tipo é mais apropriado.

OBS: O tipo None é SEMPRE especificado com a primeira letra maiúscula.

Certo: None
Errado: none

Quando utilizamos?

- Podemos utilizar None quando queremos criar uma variável e inicializá-la com um tipo sem tipo, antes de recebermos um valor final.

OBS: O tipo None em Python é SEMPRE considerado como False.

numeros = None

print(numeros)
print(type(numeros))

numeros = 1.44, 1.34, 5.67

print(numeros)
print(type(numeros))

# O método fromkeys recebe dois parâmetros: um interável e um valor.
# Ele vai gerar para cada valor do iterável uma chave e irá atribuir a esta chave o valor informado.

veja = {}.fromkeys('teste', 'valor')
print(veja)

veja = {}.fromkeys(range(1, 11), 'novo')
print(veja)
"""
