# if, elif(else if) e else são os comandos para ter várias condições

nome = str(input('Digite o seu nome: ')).upper()

if nome == 'JONATAS':
    print('QUE NOME TOP!')
    
elif nome == 'VICTORIA' or nome == 'GISELDA' or nome == 'GERALDO':
    print('QUE NOME MARAVILHOSO!')
    
elif nome in 'ANA MARIA RAUL PAULO FELIPE LUIS GUILHERME':
    print('Você é família!')
    
else:
    print('BOM NOME!')
    
print('Tenha um bom dia, {}!'.format(nome))