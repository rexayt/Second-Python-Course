"""
Métodos de Data e Hora

# Com now() podemos especificar um timezone (Fuso Horário).
agora = datetime.datetime.now() # now() == agora
print(agora)
print(type(agora))
print(repr(agora))

hoje = datetime.datetime.today() # today() == hoje
print(hoje)
print(type(hoje))
print(repr(hoje))

# Mudanças ocorrendo à meia-noite combine()

manutencao = datetime.datetime.combine((datetime.datetime.now() + datetime.timedelta(days=1)), datetime.time())

print(manutencao)
print(type(manutencao))
print(repr(manutencao))

# Encontrar o dia da semana, weekday()

# Os dias da semana do método weekday() começam em 0, sendoo esta a segunda-feira

manutencao = datetime.datetime.combine((datetime.datetime.now() + datetime.timedelta(days=1)), datetime.time())

print(manutencao.weekday())

aniversario = input('Qual a data do seu aniversário? (dd/MM/yyyy): ')

aniversario = aniversario.split('/')

aniversario = datetime.datetime(int(aniversario[2]), int(aniversario[1]), int(aniversario[0]))

if aniversario.weekday() == 0:
    print('Você nasceu numa segunda-feira')
elif aniversario.weekday() == 1:
    print('Você nasceu numa terça-feira')
elif aniversario.weekday() == 2:
    print('Você nasceu 25numa quarta-feira')
elif aniversario.weekday() == 3:
    print('Você nasceu numa quinta-feira')
elif aniversario.weekday() == 4:
    print('Você nasceu numa sexta-feira')
elif aniversario.weekday() == 5:
    print('Você nasceu num sábado')
elif aniversario.weekday() == 6:
    print('Você nasceu num domingo')

# Formatando datas/horas com strftime() (String Format Time)

hoje = datetime.datetime.today()

print(hoje)

hoje_formatado = hoje.strftime('%d/%b/%Y')

print(hoje_formatado)

def formata_data(data):
    meses = {'1': 'Janeiro', '2': 'February', '3': 'Março',
             '4': 'Abril', '5': 'Maio', '6': 'Junho', '7': 'Julho', '8': 'Agosto', '9': 'September',
             '10': 'Outubro', '11': 'Novembro', '12': 'Dezembro'}
    mes = str(data.month)
    return f'{data.day} de {meses[mes]} de {data.year}'

# Formatando datas/horas com strftime() (String Format Time)

hoje = datetime.datetime.today()

print(formata_data(hoje))

from textblob import TextBlob

def formata_data(data):
    mes = TextBlob(data.strftime("%B")).translate(from_lang='en', to='pt-br' )
    return f'{data.day} de {mes} de {data.year}'

hoje = datetime.datetime.today()

print(formata_data(hoje))

nascimento = input('Qual sua data de nascimento? (dd/mm/yyyy): ')

nascimento = datetime.datetime.strptime(nascimento, '%d/%m/%Y')

print(nascimento)

# Marcando tempo de execução do nosso código com timeit

# Loop for
tempo = timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
print(tempo)

# List Comprehension
tempo = timeit.timeit('"-".join([str(n) for n in range(100)])', number=10000)
print(tempo)

# Map
tempo = timeit.timeit('"-".join(map(str,range(100)))', number=10000)
print(tempo)

"""
import timeit, functools

def teste(n):
    soma = 0
    for num in range(n * 200):
        soma = (soma + num) ** (num + 4)
    return soma

print(timeit.timeit(functools.partial(teste, 2), number=1000))