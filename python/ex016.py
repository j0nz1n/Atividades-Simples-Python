import math

num = float(input('Digite um número: '))
numint = math.floor(num)
numint2 = math.ceil(num)

print('A porção inteira do número digitado é: '.format(math.trunc(num)))

'''
print('A porção inteira do número digitado é: {}'.format(numint))
print('A porção inteira do número digitado é: {}'.format(numint2))
print('A porção inteira do número digitado é: {:.0f}'.format(num))
'''
