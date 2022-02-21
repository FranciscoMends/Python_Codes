from math import sqrt
x = float(input('Digite um número: '))
if x < 0:
    print('Número Inválido!')
else:
    y = sqrt(x)
    print('A raiz de {} é {} !'.format(x, y))