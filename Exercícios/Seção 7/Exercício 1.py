"""
Faça um programa que possua um vetor denomidado A que armazene 6 número inteiros. O programa deve executar os seguintes passos:
    - (a) Atribua os seguintes valores a esse vetor: 1, 0, 5, -2, -5, 7.
    - (b) Armazene em uma variável inteira (simples) a soma entre os valores das posições A[0], a[1], a[5] do vetor e mostre na tela esta soma.
    - (c) Modifique o vetor na posição 4, atribuindo a esta posição o valor 100.
    - (d) Mostre na tela cada valor do vetor A, um em cada linha.
"""
vetor = [1, 0, 5, -2, -5, 7]
soma = vetor[0] + vetor[1] + vetor[5]
print('Soma = ',soma)
vetor.remove(-5)
vetor.insert(4,100)
for c in vetor:
    print(c)