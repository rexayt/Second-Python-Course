"""
Faça um programa que leia um vetor de 5 posições para números reais e, depois, um código inteiro. 
    - Se o código for zero, finalize o programa;
    - Se for 1, mostre o vetor na ordem direta;
    - Se for 2, mostre o vetor na ordem inversa.
    - Caso, o código for diferente de 1 e 2 escreva uma mensagem informando que o código é inválido
"""
lista = []
for c in range(5):
    n = int(input('Digite um número: '))
    lista.append(n)

while True:
    e = int(input(f"{'-'*45}\nEscolhas\n\t- 0 (Finalizar)\n\t- 1 (Mostrar lista organizada)\n\t- 2 (Mostrar na ordem inversa)\nDigite sua escolha: "))
    print(f'{"-"*45}')
    if e == 0:
        break
    elif e == 1:
        lista.sort()
        print(lista)
        break
    elif e == 2:
        lista.reverse()
        print(lista)
        break
    else:
        print("Erro!!!\nCódigo Inválido.")