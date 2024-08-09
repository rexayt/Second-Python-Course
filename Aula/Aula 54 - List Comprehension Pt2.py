"""
List Comprehension

Nós podemos adicionar estruturasa condicionais lógicas às nossas List Comprehension
"""

# Exemplos

# 1

numeros = [1, 2, 3 ,4 ,5, 6]

pares = [num for num in numeros if num % 2 == 0]
impares = [num for num in numeros if num % 2 != 0]

print(pares)
print(impares)

# Refatorar
# Qualquer número par módulo de 2 é 0 e 0 em Python é False. not False = True
pares = [numero for numero in numeros if not numero % 2]
impares = [numero for numero in numeros if numero % 2]

print(pares)
print(impares)

# 2

res = [numero * 2 if not numero % 2 else numero / 2 for numero in numeros]
print(res)