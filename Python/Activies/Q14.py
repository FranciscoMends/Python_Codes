a = int(input('Primeiro lado:'))
b = int(input('Segundo lado:'))
c = int(input('Terceiro lado:'))

if (a+b>c) and (a+c>b) and (b+c>a):
    if (a==b) and (b==c):
        print('Triângulo Equilátero')
    elif (a==b) or (a==c) or (c==b):
        print('Triângulo  Isóseles')
    else:
        print('Triângulo Escaleno')
else:
    print('Triãngulo Inexistente!')