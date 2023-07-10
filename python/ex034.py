sal = float(input('Digite o salário do funcionário: R$'))
if sal <= 1250:
    print('O seu salário atualizado é de R${}'.format(sal + (sal*15/100)))
else:
    print('O seu salário atualizado é de R${}'.format(sal + (sal*10/100)))
    