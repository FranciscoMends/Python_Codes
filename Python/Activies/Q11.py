import math
a = float(input('Dijite o primeiro termo: '))
b = float(input('Dijite o segundo termo: '))
c = float(input('Dijite o terceiro termo: '))

if a:
    delta = b**2 - 4*a*c
    if delta > 0:
        x1 = (-b +math.sqrt(delta)) / (2*a)
        x2 = (-b -math.sqrt(delta)) / (2*a)
        print('X1=',x1)
        print('X2=',x2)
    else:
        print('Não há raízes reais')
else:
    x1 = -c/b
    print('X1=',x1)
