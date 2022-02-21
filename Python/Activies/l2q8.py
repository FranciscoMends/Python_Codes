a = float(input('Digite a primeira nota: '))
b = float(input('Digite a segunda nota: '))
c = float(input('Digite a terceira nota: '))
d = float(input('Digite a quarta nota: '))

f = (a+b+c+d)/4
print('Média Final:',f)
if f >= 7.0:
    print('Situação: Aprovado')
else:
    print('Situação: Reprovado')
    