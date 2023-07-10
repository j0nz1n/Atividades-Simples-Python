n1 = float(input('Digite o valor do primeiro segmento: '))
n2 = float(input('Digite o valor do segundo segmento: '))
n3 = float(input('Digite o valor do terceiro segmento: '))

if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
    print('É possível formar um triângulo!')
    if n1 == n2 == n3:
        print('O triângulo é equilátero')
    elif n1 != n2 != n3 != n1:
        print('O triângulo é escaleno')
    else:
        print('O triângulo é isósceles')
else:
    print('É impossível formar um triângulo!')
