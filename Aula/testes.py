import unittest

from atividades import *

class AtividadesTestes(unittest.TestCase):

    def test_comer_saudavel(self):
        """Testando o retorno com comida saudável."""
        self.assertEqual(
            comer('quiabo', True),
            'Estou comendo quiabo porque quero manter a forma.'
        )
    
    def test_comer_gostosa(self):
        """Testando o retorno com comida gostosa."""
        self.assertEqual(
            comer(comida='pizza', eh_saudavel=False),
            'Estou comendo pizza porque a gente só vive uma vez'
            )
        
    def test_dormir_pouco(self):
        """Testando o retorno com poucas horas dormidas."""
        self.assertEqual(
            dormir(4),
            'Continuo cansado após dormir por 4 horas. :('
        )
    
    def test_dormir_muito(self):
        """Testando o retorno com muitas horas dormidas."""
        self.assertEqual(
            dormir(10),
            'Ptz! Dormi muito! Estou atrasado para o trabalho'
        )

    def test_eh_engracada(self):
        self.assertFalse(eh_engracada('Sergio Malandro'))

if __name__ == '__main__':
    unittest.main()


