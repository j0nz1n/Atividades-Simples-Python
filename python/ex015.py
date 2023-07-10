d = float(input('Por quantos dias o carro foi alugado? '))
km = float(input('Quantos km foram percorridos pelo carro alugado? '))
n1 = 0.15 * km
n2 = 60 * d
print('Você precisará de R${:.2f} para pagar o aluguel completo!'.format(n1+n2))
