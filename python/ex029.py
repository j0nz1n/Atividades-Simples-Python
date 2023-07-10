import pygame
vel = float(input('Digite a velocidade do veículo em km/h: '))
if vel>80:
    multa = 7 * (vel - 80)
    print('Você ultrapassou o limite de velocidade da via! Foi multado no valor de R${}'.format(multa))
    pygame.init()
    pygame.mixer.music.load('zatumalaka.mp3')
    pygame.mixer.music.play()
    input()
    pygame.event.wait()
else:
    print('Por aqui está tudo de boa, parceiro!')
    
print('Siga bem!')
