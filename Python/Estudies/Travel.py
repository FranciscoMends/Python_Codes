from ast import While


name = input('Qual seu nome? ')

def begin(car):
    
    print()
    print('Olá {}! Como você está?'.format(name))
    print('Este programa foi feito para você ver os devidos upgrades do seu carro!')

def what(what2):
    sn = input('Alguns não foram criados ainda deseja inserir?')
    what1 = sn.lower
    if what1 == 's':
        what2 = True
    else:
        what2 = False

def main():
    
    while True:
        begin
        if what == True:
            print('Perfeito!')
        else:
            print('Que pena...')

if __name__ == '__main__':
    main()
