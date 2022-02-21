a = int(input('Digite o primeiro valor: '))
b = int(input('Digite o segundo valor: '))
c = int(input('Digite o terceiro valor: '))
'''
if (a < b) and (a < c):
    print('O menor valor é : {}!'.format(a))
elif (b < c):
    print('Omenor valor é: {}!'.format(b))
else:
    print('O menor valor é: {}!'.format(c))
'''

print('O menor valor é: {}!'.format(min(a, b, c)))
