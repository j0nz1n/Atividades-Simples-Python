somaidades = 0
maisvelho = 0
mulheresmenores = 0
homemvelho = 'NÃO HÁ HOMENS NA LISTA'
for i in range(1,5):
    print('----- {}ª PESSOA -----'.format(i))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()
    somaidades = somaidades + idade
    media = somaidades / 4
    if idade > maisvelho and sexo == 'M':
        maisvelho = idade
        homemvelho = nome
    if idade < 20 and sexo == 'F':
        mulheresmenores = mulheresmenores + 1
        
print('A média de idade do grupo é de {} anos'.format(media))
print('O homem mais velho tem {} anos e se chama: {}'.format(maisvelho,homemvelho))
print('Há {} mulheres menores de 20 anos'.format(mulheresmenores))
