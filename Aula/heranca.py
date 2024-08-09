"""
POO - Herança (Inheritance)

A ideia de herança é a de reaproveitar código. Também extender nossas classes.

OBS: Com a herança, a partir de uma classe existente, nos extendemos outra classe
que passa a herdar atributos e métodos da classe herdada.

Quando uma classe herda de outra classe, a classe herdada é conhecida por:
    - Super Classe
    - Classe mãe;
    - Classe pai;
    - Classe base;
    - Classe Genérica;

Quando uma classe herda de outra classe, ela é chamada:
    [Cliente, Funcionario]
    - Sub classe;
    - Classe filha;
    - Classe específica;

# Sobrescrita de métodos, ocorre quando reescrevemos um método presente na super classe
em classes filhas


"""

class Pessoa:

    def __init__(self, nome, sobrenome, cpf):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'


class Cliente(Pessoa):

    def __init__(self, nome, sobrenome, cpf, renda):
        super().__init__(nome, sobrenome, cpf)
        self.__renda = renda

class Funcionario(Pessoa):
    
    def __init__(self, nome, sobrenome, cpf, matricula):
        super().__init__(nome, sobrenome, cpf)
        self.__matricula = matricula

    def nome_completo(self):
        print(self._Pessoa__cpf)
        return f'Funcionário: {self.__matricula} Nome: {self._Pessoa__sobrenome}'

class Pinguim:

    def __init__(self, nome, sobrenome):
        self.__nome = nome
        self.__sobrenome = sobrenome


# Sobrescrita de métodos (Overriding)

cliente1 = Cliente('Angelina', 'Jolie', '123.456.789-00', 5000)
funcionario1 = Funcionario('Felicity', 'Jones', '987.654.321-11', 1234)

print(cliente1.nome_completo())
print(funcionario1.nome_completo())