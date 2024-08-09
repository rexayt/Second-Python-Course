# def cumprimentar(nome: str) -> str:
#     return f"Olá"

# print(cumprimentar('Geek'))

# def cabecalho(texto:str, alinhamento:bool=True) -> str:
#     if alinhamento:
#         return f'{texto.title()}\n{"-" * len(texto)}'
#     else:
#         return f"{texto.title()}".center(50, '#')
    
# print(cabecalho('Geek University'))

# print(cabecalho('Geek University', False))

# def cabecalho(texto: str, alinhamento: bool =True) -> str:
#     if alinhamento == True:
#         return f'{texto.title()}\n{"-" * len(texto)}'
#     elif alinhamento == False:
#         return f"{texto.title()}".center(50, '#')
#     else:
#         raise TypeError('Aí parcero é só True ou False')
# print(cabecalho('Geek University'))

# cabecalho('Geek University', alinhamento=True)

class Pessoa:

    def __init__(self, nome: str, idade: int, peso: float) -> None:
        self.__nome: str = nome
        self.__idade: int = idade
        self.__peso: float = peso

    def andar(self) -> str:
        return f'{self.__nome} está andando'
    
p = Pessoa('Alex', 23, 69)

print(p.andar())