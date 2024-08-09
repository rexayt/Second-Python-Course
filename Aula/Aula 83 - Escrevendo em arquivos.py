"""
Escrevendo em arquivos

# OBS: Ao abrir um arquivo para leitura, não podemos realizar a escrita nele. Apenas ler.
Da mesma forma, se abrirmos um arquivo para escrita, não podemos lê-lo, somente escrever nele.

# OBS: Ao abrir um arquivo para escrita, o arquivo é criado no sistema operacional.

Para escrevermos dados em um arquivo, após abrir o arquivo utilizamos a função write().
Esta função recebe uma string como parâmetro, caso contrário teremos um TypeError.

Abrindo um arquivo para escrito com o modo 'w', se o arquivo não existir será criado,
caso ele já exista o, anterior será apagado e um novo será criado. Dessa forma, todo
o conteúdo no arquivo anterior é perdido.

# Exemplo de escrita - modo 'w' - write (escrita)

with open('Aula/novo.txt', 'w', encoding='utf-8') as arquivo:
    arquivo.write('Novos dados\n')
    arquivo.write('Outros podemos colocar quantas linhas quisermos.\n')
    arquivo.write('Mais Esta é a última linha.\n')


# Forma tradicional de escrita em arquivo (Não Pythônica)
arquivo = open('Aula/mais.txt', 'w', encoding='utf-8')

arquivo.write('Um texto qualquer.\n')
arquivo.write('Mais um texto.\n')

arquivo.close()

with open('geek.txt', 'w', encoding='utf-8') as arquivo:
    arquivo.write('Geek\n'*1000)
"""

with open('frutas.txt', 'w', encoding='utf-8') as arquivo:
    while True:
        fruta = input('Informe a fruta ou digite sair: ')
        if fruta != 'sair':
            arquivo.write(f'{fruta}\n')
        else:
            break