# ALUNOS:
# Felisberto Teixeira Bastos Neto
# Francisco Mendes Magalhães Filho
# Tiago da Silva Carvalho

def code(digito):

    list1 = digito.replace('-', ' ').replace('' ,' ').replace('X', '10')
    list2 = digito.replace('-', '').replace('X', '10').replace(' ' ,'')
    result = digito.replace(' ' ,'')


    if not list2.isnumeric():
        print(result, 'está incorreto.')
    else:
        lista = list1.split()
        listf = list(map(int, lista))
        contag = len(listf)
        print(listf)
        if contag != 10:
            print(result, 'está incorreto.')
        else:

            # analisador
            cont = 0
            analisadorf = 0
            x = 10
            while cont < 10:
                analisador = listf[cont] * x
                 cont += 1
                x -= 1
                analisadorf = analisadorf + analisador

            # certificador
            certificador = analisadorf % 11
            if certificador == 0:
                print(result, 'está correto.')
            else:
                print(result, 'está incorreto.')

def main():
    
    while True:
        isbn_code = input().strip()

        if isbn_code == '0-00000-000-0':
            break

        code(isbn_code)


if __name__ == '__main__':
    main()

    