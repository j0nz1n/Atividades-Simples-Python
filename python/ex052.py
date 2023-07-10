n = int(input('Digite um número: '))
divisivel = False
for i in range(2,n):
    print(i, end = ' ')
    
    if n % i == 0:
        divisivel = True
    
if divisivel == True:
    print('\nNão é primo')
else:
    print('É primo')
