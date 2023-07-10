print('{:=^40}'.format(' LOJAS JON '))

preço = float(input('Preço das compras: R$'))
forma = int(input(' [1] À vista dinheiro \n [2] À vista cartão \n [3] 2x no cartão \n [4] 3x ou mais no cartão \n'))
if forma == 1:
    print('você recebeu um desconto e irá pagar: R${}'.format(preço - preço*(10/100)))
elif forma == 2:
    print('você recebeu um desconto e irá pagar: R${}'.format(preço - preço*(5/100)))
elif forma == 3:
    print('você irá pagar: R${}'.format(preço))
elif forma == 4:
    print('você recebeu juros e irá pagar: R${}'.format(preço + preço*(20/100)))
else:
    print('OPÇÃO INVÁLIDA')
