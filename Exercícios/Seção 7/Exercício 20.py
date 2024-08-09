"""
Escreva um programa que leia números inteiros no intervalo [0,50] e os armazene em um vetor com 10 posições.
Preencha um segundo vetor apenas com os números ímpares do primeiro vetor.
Imprima os dois vetores, 2 elementos por linha.
"""
from random import randint
lista = []
im = []
for c in range(10):
   ra = randint(0,50)
   lista.append(ra)
   if ra % 2 != 0:
      im.append(ra)
print(f'Impar = {im}, Lista = {lista}')