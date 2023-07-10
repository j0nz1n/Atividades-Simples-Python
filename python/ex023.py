'''
n = str(input('Digite um número inteiro até 9999: '))
n.strip()
print('Unidade: {}'.format(n[3]))
print('Dezena: {}'.format(n[2]))
print('Centena: {}'.format(n[1]))
print('Milhar: {}'.format(n[0]))
'''

#O jeito normal exije estrutura de repetição!

n = int(input('Digite um número inteiro até 9999: '))
u = n//1 % 10
d = n//10 % 10
c = n//100 % 10
m = n//1000 % 10

print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))
