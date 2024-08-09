"""
Teste de memória com Generators

# Sequência de Fibonacci

# Teste
for n in fib_lista(100000):
    print(n)




"""

# Função usando listas 481 MB
 
def fib_lista(max):
    nums = []
    a, b = 0, 1
    while len(nums) < max:
        nums.append(b)
        a, b = b, a+b
    return nums

# Função com generator 4 MB

def fib_gen(max):
    a, b, contador = 0, 1, 0
    while contador < max:
        a, b = b, a+b
        yield a
        contador += 1



for n in fib_gen(100):
    print(n)