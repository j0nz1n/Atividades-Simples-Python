import random

player = int(input(' [0] Pedra \n [1] Papel \n [2] Tesoura \n Digite a sua opção: '))
lista = [0, 1, 2]
pc = random.choice(lista)

if 0 < player > 2:
    print('OPÇÃO INVÁLIDA!')

elif player == pc:
    print('Empatou!')
    
    
elif player == 0 and pc == 2:
    print('Você venceu! O computador jogou tesoura')
    
elif player == 0 and pc == 1:
    print('Você perdeu! O computador jogou papel')
    
    
elif player == 1 and pc == 0:
    print('Você venceu! O computador jogou pedra')
    
elif player == 1 and pc == 2:
    print('Você perdeu! O computador jogou tesoura')

    
elif player == 2 and pc == 0:
    print('Você perdeu! O computador jogou pedra')
    
elif player == 2 and pc == 1:
    print('Você venceu! O computador jogou papel')
