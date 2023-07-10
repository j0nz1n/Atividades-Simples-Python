casa = float(input('Valor da casa: R$'))
sal = float(input('Salário do comprador: R$'))
anos = int(input('Anos de financiamento: '))
prestação = casa / (anos*12)

print('A prestação será de R${:.2f}'.format(prestação))

if prestação > sal * 30 / 100:
    print('Empréstimo negado')
else:
    print('Empréstimo aprovado')
    