'''
nome = input('Insira seu nome: ')
if nome == 'Mendes':
    print('Que nome lindo você tem!')
else:
    print('Seu nome é tão normal!')
print('Bom dia {}!'.format(nome))
'''
#DESAFIO_28
'''
from random import randint
from time import sleep
x = randint(0,5)
y = int(input('Digite um número de 0 à 5: '))
print('Loading...')
sleep(2)
if x == y:
    print('Parabéns, você venceu!')
else:
    print('Tente novamente, você perdeu!')
print(x)
'''
#DESAFIO_29
'''
velocity = int(input('Qual a velocidade atual do seu carro em Km/h? '))
if velocity > 80:
    print('Você foi multado por excesso de velocidade!')
    print('Velocidade permitia: 80km/h')
    print('Velocidade ultrapassada: {}km/h'.format(velocity))
    infraction = (velocity - 80) * 7
    print('Valor da multa: R${},00'.format(infraction))    
'''
#DESAFIO_30
'''
number = int(input('Insira um número inteiro: '))
if number % 2 == 0:
    print('Seu número é PAR!')
else:
    print('Seu número é ÍMPAR!')
'''
#DESAFIO_31
'''
distance = int(input('Qual a distância em Km que deseja viajar? '))
if distance <= 200:
    final_value = distance * 0.50
else:
    final_value = distance * 0.45
print('Valor da passagem: R${:.2f}'.format(final_value))
'''
#DESAFIO_32
'''
from datetime import date
year = int(input('Insira um ano (Coloque "0" caso queira analisar a data atual): '))
if year == 0:
    year = date.today().year    
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print(year, 'é um ano BISSEXTO!')
else:
    print(year, 'não é um ano BISSEXTO!')
'''
#DESAFIO_33
'''
x = int(input('Digite o primeiro número: '))
y = int(input('Digite o segundo número: '))
z = int(input('Digite o terceiro número: '))

number_max = max(x,y,z)
number_min = min(x,y,z)

print('Maior número:',number_max)
print('Menor número:',number_min)
'''
#DESAFIO_34
'''
wage = float(input('Insira seu salário: R$'))
if wage > 1250:
    salary_increase = ((10/100) * wage) + wage
    percent = 10
else:
    salary_increase = ((15/100) * wage) + wage
    percent = 15
print()
print('Salário atual: R${:.2f}'.format(wage))
print('Aumento de {}%'.format(percent))
print('Salário final: R${:.2f}'.format(salary_increase))
'''
#DESAFIO_35
'''
line1 = float(input('Insira o comprimento da primeira reta: '))
line2 = float(input('Insira o comprimento da segunda reta: '))
line3 = float(input('Insira o comprimento da terceira reta: '))

if line1 < line2 + line3 and line2 < line1 + line3 and line3 < line1 + line2:
    print('Podem formar um triângulo!')
else:
    print('Não podem formar um triângulo!')
'''
#PROVA
'''
s = 'prova de python'
x = len(s)
print(x)

x = 'curso de python no cursoemvideo'
y = x[:5]
print(y)
'''
x = 3 * 5 + 4 ** 2
print(x)