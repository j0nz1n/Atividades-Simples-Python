pesado = 0
leve = 99999
for i in range (1, 6):
    peso = float(input('Digite o peso da {}ª pessoa (KG): '.format(i)))
    if peso >= pesado:
        pesado = peso
    elif peso <= leve:
        leve = peso
print('O maior peso lido foi de {}KG e o menor peso lido foi de {}KG'.format(pesado, leve))
