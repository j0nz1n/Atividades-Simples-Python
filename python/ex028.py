import random
import pygame
import time
lista = [0, 1, 2, 3, 4, 5]
pc = random.choice(lista)

print('-=-' * 10)
print('Pensando em um número...')
time.sleep(2)
print('Pensei!')
print('-=-' * 10)
escolha = int(input('Tente advinhar o número que o PC pensou (entre 0 e 5)! Digite: '))
print('-=-' * 10)

print('O número escolhido foi: {}!'.format(pc))
if escolha == pc:
    print('Você venceu, seu marginalzinho noggers!')
else:
    print('Você perdeu, SEU ATUMALAKS!')
    
    pygame.init()
    pygame.mixer.music.load('zatumalaka.mp3')
    pygame.mixer.music.play()
    input()
    pygame.event.wait()
print('-=-' * 10)   