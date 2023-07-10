distancia = float(input('Distância da viagem: '))
if distancia <= 200:
    print('A sua passagem custará: R${:.2f}'.format(distancia * 0.50))
else:
    print('A sua passagem custará: R${:.2f}'.format(distancia * 0.45))
