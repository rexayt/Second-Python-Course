# Faça um vetor de tamanho 50 preenchido com o seguinte valor: (i+5*i)%(i+1), sendo i a posição do elemento no vetor. Em seguida imprima o vetor na tela.
lista = []
for vetor in range(50):
    lista.append((vetor + 5 * vetor)%(vetor + 1))
print(lista)