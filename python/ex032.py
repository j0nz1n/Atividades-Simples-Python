import datetime
ano = int(input('Digite um ano: '))

if ano == 0:
    ano = datetime.date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('{} É bissexto!'.format(ano))
else:
    print('{} Não é bissexto!'.format(ano))