n1 = float(input('Digite a primeira nota do aluno: '))
n2 = float(input('Digite a segunda nota do aluno: '))
media = (n1 + n2) / 2

print('A sua média foi: {}'.format(media))

if media < 5:
    print('Reprovado')
elif 5 <= media <= 6.9:
    print('Recuperação')
else:
    print('Aprovado')
