import math
a = float(input('insira um ângulo: '))
sen = math.sin(math.radians(a))
cos = math.cos(math.radians(a))
tan = math.tan(math.radians(a))
print('O seno do ângulo de {}° é: {:.2f}'.format(a, sen))
print('O cosseno do ângulo de {}° é: {:.2f}'.format(a, cos))
print('A tangente do ângulo de {}° é: {:.2f}'.format(a, tan))
