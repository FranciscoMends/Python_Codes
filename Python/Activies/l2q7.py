a = float(input('Digite a primeira nota: '))
b = float(input('Digite a segunda nota: '))
c = float(input('Digite a terceira nota: '))
print()
print()
print('Selecione uma opção:')
print('1- Calcular a média aritmética.')
print('2- Soma dos valores.')
print('3- Fazer teste no segundo valor.')
p = int(input('Digite aqui a opção escolhida: '))
print()
if p == 1:
    print('Média Aritmética:',(a+b+c)/3)
elif p == 2:
    print('Soma dos Valores:',(a+b+c))
elif p == 3:
    x = b%2
    if x == 0:
        print('Teste: {} é par!'.format(b))
    else:
        print('Teste: {} é impar!'.format(b))
else:
    print('Operação Inválida!')
