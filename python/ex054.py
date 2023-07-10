import datetime

velhos = []
novos = []
for i in range (1, 8):
    n = int(input('Digite o ano de nascimento da {}ª pessoa: '.format(i)))
    
    if datetime.date.today().year - n <= 18:
        novos.append(n)
    else:
        velhos.append(n)
print('existem {} maiores de idade e {} menores de idade'.format(len(velhos), len(novos)))
