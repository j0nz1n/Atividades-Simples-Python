n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))
n3 = float(input('Digite o terceiro número: '))
menor = n1
maior = n1

if menor > n2:
    menor = n2
if menor > n3:
    menor = n3
if maior < n2:
    maior = n2
if maior < n3:
    maior = n3
print('O maior número é {} e o menor é {}'.format(maior, menor))
 