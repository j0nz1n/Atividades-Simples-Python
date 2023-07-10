import datetime
ano = int(input('Informe o seu ano de nascimento: '))
idade = datetime.date.today().year - ano

if idade <= 9:
    print('Você tem {} anos e é um atleta mirim'.format(idade))
elif 9 < idade <= 14:
    print('Você tem {} anos e é um atleta infantil'.format(idade))
elif 14 < idade <= 19:
    print('Você tem {} anos e é um atleta júnior'.format(idade))
elif 19 < idade <= 25:
    print('Você tem {} anos e é um atleta sênior'.format(idade))
elif idade > 25:
    print('Você tem {} anos e é um atleta master'.format(idade))
