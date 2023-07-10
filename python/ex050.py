soma = 0
for i in range (0,6):
    n=int(input('Digite um número: '))
    if n % 2 == 0:
        soma = soma + n
print('A soma dos pares é: {}'.format(soma))
