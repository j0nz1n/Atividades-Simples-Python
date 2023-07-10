frase = str(input('Digite uma frase: '))
frase = frase.upper()
frase = frase.replace(' ', '')
frase_contrario = frase[::-1]

if frase == frase_contrario:
    print('PALÍNDROMO')
else:
    print('NOPE')