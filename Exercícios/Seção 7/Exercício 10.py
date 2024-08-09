# Faça um programa para ler a nota da prova de 15 alunos e armazene num vetor, calcule e imprima a média geral
lista = []
for c in range(1,16):
    lista.append(int(input(f'Digite a nota do {c}º aluno: ')))
media = sum(lista) / 15
print(f'A média foi {media:.2f}')