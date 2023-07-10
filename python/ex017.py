import math
cato = float(input('Qual é o comprimento do cateto oposto em centímetros? '))
cata = float(input('Qual é o comprimento do cateto adjacente em centímetros? '))
h = math.hypot(cato, cata)
#h = math.sqrt(cato**2 + cata**2)
print('A hipotenusa é: {:.2f}'.format(h))
