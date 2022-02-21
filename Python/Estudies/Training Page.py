#-----------------------------------------------------------------------------------
# OPERADORES
# (+) (-) (*) (/)
# (//) divisão interira  ex. 2,5 == 2 
# (%) resto da divisão   ex. 2,5 == 5
# (**) elevação  ex. 3**2 == 9
# import math (math.sqrt) raiz quadrada
# Ou 
# from math import sqrt
# Ou
# x**(1/2) == raiz quadrada de x
# x**(1/3) == raiz cúbica de x
#
#print = escreva                                              
print('Olá mundo!') # aspas para strings                                       (>) direita
print('Olá {:=^20}!'.format('ana')) # (:20) espaços pro lado.  (=)simbolo pa-  (^) centralizado   
print('Oi'+'Olá') # junta (OI+OLA = OIOLA)                      ra os espaços  (<) esquerda
print('Oi'*5) # string se repete 5 vezes (OIOIOIOIOI)
print(2+3) # sem aspas para numeros
print('2'+'3') # '+' junta as strings sem espaço
print('2','3') # ',' junta as strings dando um espaço
print('2',' ','3') # para mais espaço entre strings
print('-' * 30) # repete uma string 30 vezes
print(1,2,3,4,sep='---') # customizar serparadores de qualquer elemento
print('Olá mundo!',end=' ') # continua na mesma linha
print('Olá mundo!',end='\n\n\n') # pula linhas
print('Olá mundo!')
h = 'HOMEM'
print(h.lower()) # 'HOMEM' sai minusculo (homem)
i = 'mulher'
print(i.upper()) # 'mulher' sai maiusculo (MULHER)
print()
j = 1.55555                           # 1.55555 == 1.56
print('O valor é: {:.2f}!'.format(j)) # seleciona o num de casas após a virgula 
print()                               # (aproximando do valor exato do numero)
print() # também pula linhas
print()
#-----------------------------------------------------------------------------------
# VARIÁVEIS
nome1 = 'Mendes' # declarando uma string
idade1 = 20 # declarando um número
peso1 = 62.8
print(nome1,idade1,peso1,sep=' - ')
#-----------------------------------------------------------------------------------
# VARIÁVEIS LIDAS (INPUT)
'''
nome2 = input('Qual seu nome? ') # declarando uma string interativa / input = leia uma palavra ou frase
idade2 = int(input('Qual sua idade?')) # declarando um número interativo / input(int()) = leia um número
peso2 = float(input('Qual seu peso? ')) # 'float' = ponto flutuante (real)
print('Nome: ',nome2)
print('Idade: ',idade2)
print('Peso: ',peso2)
'''
#-----------------------------------------------------------------------------------
# TIPO PRIMITIVO
a = input('Digite algo: ')
print(type(a))
n = (a.isnumeric())
if n == True:
    print('Tipo primitivo: Numérico')
n = (a.isalnum()) #(alfabetos ou números)
if n == True:
    print('Tipo primitivo: Alnum')
n = (a.isalpha())
if n == True:
    print('Tipo primitivo: Alfabético')
n = (a.isascii()) #string vazia ou ASCII
if n == True:
    print('Tipo primitivo: Ascii')
n = (a.isdecimal())
if n == True:
    print('Tipo primitivo: Decimal')
n = (a.isdigit()) #dígitos sem pontuação
if n == True:
    print('Tipo primitivo: Dígitos')
n = (a.isidentifier()) #dígitos_com_espaço_utilizando "_"
if n == True:
    print('Tipo primitivo: Identifier')
n = (a.islower()) # todas letras minúsculas
if n == True:
    print('Tipo primitivo: Slower')
n = (a.isprintable()) #dígitos que foram impressos (print)
if n == True:
    print('Tipo primitivo: Printable')
n = (a.isspace()) #espaço vazio
if n == True:
    print('Tipo primitivo: Space')
n = (a.istitle()) #primeiro caracter de cada palavra é maiúsculo
if n == True:
    print('Tipo primitivo: Title') 
n = (a.isupper()) #tudo maiúsculo 
if n == True:
    print('Tipo primitivo: Upper')
#-----------------------------------------------------------------------------------
# MÓDULOS IMPORTADOS
#MATH
import math #importa o pacote todo
math.sqrt
#ou
from math import ceil, factorial, floor, sqrt, trunc #importa uma função específica do pacote
sqrt # raiz quadrada
ceil # arredondar número quebrado para cima
floor # arredondar número quebrado para baixo
trunc # eliminar vígula de um número quebrado
pow # potência == "**"
factorial # calcula fatorial
#-----------------------------------------------------------------------------------
# RANDOM
import random
num1 = random.random() # número aleatório entre 0 e 1 (quebrado)
num2 = random.randint(1,10) # número aleatório entre 0 e 10 (inteiro)
print(num1)
print(num2)
#-----------------------------------------------------------------------------------
# CORES
#Exemplo: \033[x;y;zm
# x(esquerda) == style
'''
Style =>
0 = none
1 = bold (negrito)
4 = underline (sublinhado)
7 = negative (inverte)
'''
# y(meio) == text(color) 
'''
Text =>
30 = branco
31 = vermelho
32 = verde
33 = amarelo
34 = azul
35 = roxo
36 = ciano
37 = cinza
'''
# z(direita) == back(fundo)
'''
Back =>
40 = branco
41 = vermelho
42 = verde
43 = amarelo
44 = azul
45 = roxo
46 = ciano
47 = cinza
'''
