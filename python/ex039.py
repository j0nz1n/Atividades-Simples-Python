import datetime
ano = int(input('Ano de nascimento: '))
idade = datetime.date.today().year - ano

print('Você tem {} anos de idade!'.format(idade))

if idade < 18:
    print('Ainda não está na hora de se alistar! faltam {} anos'.format(18 - idade))
    print('Seu alistamento deverá ser realizado em {}'.format(ano + 18))
elif idade > 18:
    print('Já passou da hora de se alistar! Você está {} anos atrasado'.format(idade - 18))
    print('Seu alistamento deveria ser realizado em {}'.format(ano + 18))
else:
    print('É a hora de se alistar!')
