"""
Geradores

- Geradores (Generators) são Iterators (Iteradores)

OBS: O contrário não é verdadeiro. Ou seja, nem todo iterator é um generator

Outras informações:
- Generators podem ser criados com funções geradoras:
- Funções geradoras utilizam a palavra reservada yield
- Generators podem ser criados com Expressões Geradoras;

Diferenças entre Funções e Generator Functions (Funções Geradoras)


-------------------------------------------------------------------------------------
| Funções                               | Generator Functions                       |
-------------------------------------------------------------------------------------
| utilizam return                       | Utilizam yield                            |
-------------------------------------------------------------------------------------
| retorna uma vez                       | podem utilizar yield múltiplas vezes      |
-------------------------------------------------------------------------------------
| quando executada, retorna um valor    | quando executada, retorna um generatory   |
------------------------------------------------------------------------------------
"""

# Exemplo Generator Function (Generator Function)

def conta_ate(valor_maximo):
    contador = 1
    while contador <= valor_maximo:
        yield contador
        contador = contador + 1

# OBS: Uma Geberator Function não é um Generator. Ela gera um generator. ok?
        
gen = conta_ate(10)



