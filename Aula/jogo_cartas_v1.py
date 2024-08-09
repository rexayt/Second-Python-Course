# nomes: list = ['Geek', 'University']

# versoes: tuple = ('Geek', 'University')

# dicionario: dict = {'geek': 'Geek', 'u niversity': 'University'}

# valores: set = {'Geek', 'University'}

# print(nomes)
# print(versoes)
# print(dicionario)
# print(valores)
# print(__annotations__)


# from typing import Dict, List, Tuple, Set

# nomes: List[str] = ['Geek', 'University']

# versoes: Tuple[str, str] = ('Geek', 'University')

# dicionario: Dict[str, str] = {'geek': 'Geek', 'university': 'University'}

# valores = Set[str] = {'Geek', 'University'}

# print(nomes)
# print(versoes)
# print(dicionario)
# print(valores)
# print(__annotations__)

import random

NAIPES = '♣ ♦ ♤ ♡'.split()
CARTAS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

def criar_baralho(aleatorio=False):
    """Cria um baralho com 52 cartas."""
    baralho = [{n: c} for c in CARTAS for n in NAIPES]
    if aleatorio:
        random.shuffle(baralho)
    return baralho

def distribuir_cartas(baralho):
    """Gerencia a mão de cartas de acordo com o baralho gerado."""
    return (baralho[0::4], baralho[1::4], baralho[2::4], baralho[3::4])


def jogar():
    """Inicia um jogo de cartas para quatro jogadores."""
    cartas = criar_baralho(True)
    jogadores = 'P1 P2 P3 P4'.split()
    maos = {n: m for n, m in zip(jogadores, distribuir_cartas(cartas))}

    for jogador, cartas in maos.items():
        carta = ' '.join(f"{j}" for j, in cartas)
        print(f'{jogador}: {carta}')

if __name__ == '__main__':
    jogar()