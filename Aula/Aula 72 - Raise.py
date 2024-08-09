"""
Levantando os próprios erros com raise

raise -> Lança exceções

OBS: O raise não é uma função. É uma palavra reservada, assim como def ou qualquer outra em Python.

Para simplificar, pense no raise como sendo útil para que possamos criar nossas próprias exceções e mensagens de erro.

A forma geral de utilização é:

raise TipoDoErro('Mensagem de erro')

# Exemplo real

def colore(texto, cor):
    if type(texto) is not str:
        raise TypeError('texto precisa ser uma string')
    elif type(cor) is not str:
        raise TypeError('cor precisa ser uma string')
    print(f'O text {texto} será impresso na cor {cor}')

colore('Geek', 'azul')

# Exemplo refatorado

def colore(texto, cor):
    cores = {'verde':'32','vermelho': '31', 'amarelo':'33','azul':'34','roxo':'35', 'azul claro':'36', 'cinza':'37'}
    if type(texto) is not str:
        raise TypeError('texto precisa ser uma string')
    elif type(cor) is not str:
        raise TypeError('cor precisa ser uma string')
    elif cor not in cores.keys():
        raise ValueError(f'A cor precisa ser uma entre: {cores.keys()}')
    print(f'O texto \033[0;{cores[cor]}m{texto}\033[m será impresso na cor {cor}')

texto = input('Digite o texto a ser impresso: ')
cor = input('Digite uma cor para ser impressa: ')
colore(texto, cor)

OBS: O raise, assim como o return, finaliza a função. Ou seja, nada após o raise é executador.
"""

# Exemplo real


def colore(texto, cor):
    cores = {'verde':'32','vermelho': '31', 'amarelo':'33','azul':'34','roxo':'35', 'azul claro':'36', 'cinza':'37'}
    if type(texto) is not str:
        raise TypeError('texto precisa ser uma string')
    elif type(cor) is not str:
        raise TypeError('cor precisa ser uma string')
    elif cor not in cores.keys():
        raise ValueError(f'A cor precisa ser uma entre: {cores.keys()}')
    print(f'O texto \033[0;{cores[cor]}m{texto}\033[m será impresso na cor {cor}')

texto = input('Digite o texto a ser impresso: ')
cor = input('Digite uma cor para ser impressa: ')
colore(texto, cor)