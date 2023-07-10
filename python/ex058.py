import random
import pygame
import time
tentativas = 0
lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pc = random.choice(lista)
print('-=-' * 10)
print('Pensando em um número...')
time.sleep(2)
print('Pensei!')
print('-=-' * 10)
escolha = int(input('Tente advinhar o número que o PC pensou (entre 0 e 10)! Digite: '))
print('-=-' * 10)

while escolha != pc:
    tentativas += 1
    if escolha < pc:
        escolha = int(input('ERRADO! O PC pensou em um número maior! Digite: '))
    else:
        escolha = int(input('ERRADO! O PC pensou em um número menor! Digite: '))
        
print('VOCÊ VENCEU E PRECISOU DE {} TENTATIVAS'.format(tentativas))
print('-=-' * 10)   