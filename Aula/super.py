"""
POO - O método super()

O método super() se refere á super classe.



"""

class Animal:

    def __init__(self, nome, especie):
        self.__nome = nome
        self.__especie = especie

    def faz_som(self, som):
        print(f'Este animal fala com {som}')

    
class Gato(Animal):

    def __init__(self, nome, especie, raca):
        Animal.__init__(self, nome, especie)
        super().faz_som('Au au au au')
        self.__raca = raca

felix = Gato('Felix', 'Felino' , 'Angorá')

felix.faz_som('Miau')