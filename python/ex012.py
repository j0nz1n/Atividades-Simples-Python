produto = float(input('Quanto custa o produto? R$'))
desconto = produto - produto*(5/100)
print('O produto que custava R${}, fica a {:.2f} com 5% de desconto!'.format(produto, desconto))
