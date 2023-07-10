n = int(input('Digite um número inteiro: '))
opção = int(input(' [1] converter para BINÁRIO \n [2] converter para OCTAL \n [3] converter para Hexadecimal \n Digite a sua opção: '))

if opção == 1:
    print('O número digitado em binário é: {}'.format(bin(n).replace("0b","")))
elif opção == 2:
    print('O número digitado em octal é: {}'.format(oct(n).replace("0o","")))
elif opção == 3:
    print('O número digitado em hexadecimal é: {}'.format(hex(n).replace("0x","")))
else:
    print('Comando inexistente')
    