peso = float(input('Digite o seu peso em kg:  '))
altura = float(input('Digite a sua altura em metros: '))
imc = peso / (altura * altura)

print('Seu IMC é: {:.2f}'.format(imc))

if imc < 18.5:
    print('Abaixo do peso')
elif 18.5 <= imc < 25:
    print('Peso ideal')
elif 25 <= imc < 30:
    print('Sobrepeso')
elif 30 <= imc < 40:
    print('Obesidade')
else:
    print ('Obesidade mórbida')
