nome = str(input('Digite o seu nome completo: '))
separa = nome.split()

nome.strip()

print('Seu nome com as letras maiúsculas é: {}'.format(nome.upper()))

print('Seu nome com as letras minúsculas é: {}'.format(nome.lower()))

print('No seu nome há {} caracteres sem contar os espaços'.format(len(nome)-nome.count(' ')))

print('No seu primeiro nome tem {} letras'.format(nome.find(' ')))

#print('No seu primeiro nome tem {} letras'.format(len(separa[0])))
