# Fazer um programa para ler 5 valores e, em seguida, mostrar todos os valores lidos juntamente com o maior, o menor e a média dos valores.
lista = []
for c in range(1, 6):
    n = int(input("Digite um número: "))
    lista.append(n)
    if c == 1:
        ma = me = n
    elif n > ma:
        ma = n
    elif n < me:
        me = n
media = sum(lista) / 5
print(f'A média é {media:.2f}, o maior número é {ma}, o menor número é {me}')