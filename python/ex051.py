t = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão da PA: '))
decimo = t + (10-1) * r
for i in range (t, decimo + r, r):
    print(i)
print('FINAL')