soma = 0
contador = 0
for i in range(1,501,2):
        if i % 3 == 0:
                contador += 1
                soma += i
print('a soma de todos os {} valores ímpares múltiplos de três é: {}'.format(contador, soma))
