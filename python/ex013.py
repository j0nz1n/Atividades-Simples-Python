sal = float(input('Qual é o salário atual do funcionário? R$'))
aumento = sal + (sal*15/100)
print('O salário de R${} vai para R${:.2f} com o aumento de 15%'.format(sal, aumento))
