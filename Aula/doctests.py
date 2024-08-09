"""
Doctests

Doctests são testes que colocamos na docstring das fuções/métodos Python;

Para rodar um test do doctest:

def soma(a, b):
    Soma os número a e b
    
    #>>> soma(1, 2)
    #3
    return a + b

print(soma(3, 4)) # 7

# Outro Exemplo, Aplicando o TDD

def duplicar(valores):
    #duplica os valores em uma lista


    #>>> duplicar([1, 2, 3, 4])
    #[2, 4, 6, 8]

    #>>> duplicar([])
    #[]

    #>>> duplicar(['a', 'b', 'c'])
    
    #>>> duplicar([True, None])
    #Traceback (most recent call last):
    #    ...
    #TypeError: unsupported operand type(s) for *: 'int' and 'NoneType'

    #return [2 * elemento for elemento in valores]

print(duplicar([True, None]))

# Erro inesperado...

def fala_oi():
    Fala oi
    
    #>>> fala_oi()
    #'oi'
    
    #
    return "oi"

"""

# Um último caso estranho

def verdade():
    """Retorna verdade
    
    >>> verdade()
    True
    """
    return True