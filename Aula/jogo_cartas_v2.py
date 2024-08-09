import random

NAIPES = '♣ ♦ ♤ ♡'.split()
CARTAS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

def criar_baralho(aleatorio: bool=False) -> list:
    """Cria um baralho com 52 cartas."""
    baralho = [{n: c} for c in CARTAS for n in NAIPES]
    if aleatorio:
        random.shuffle(baralho)
    return baralho

def distribuir_cartas(baralho: list) -> str:
    """Gerencia a mão de cartas de acordo com o baralho gerado."""
    return (baralho[0::4], baralho[1::4], baralho[2::4], baralho[3::4])


def jogar() -> None:
    """Inicia um jogo de cartas para quatro jogadores."""
    cartas = criar_baralho(True)
    jogadores = 'P1 P2 P3 P4'.split()
    maos = {n: m for n, m in zip(jogadores, distribuir_cartas(cartas))}

    for jogador, cartas in maos.items():
        carta = ' '.join(f"{j}" for j, in cartas)
        print(f'{jogador}: {carta}')

if __name__ == '__main__':
    jogar()