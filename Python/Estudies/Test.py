print('Olá! Como você está?')
name = input('Qual seu nome? ')
def finished():
    print('Obrigado por nos consultar, volte sempre!!!')
def menu():
    print('Seja Bem Vindo(a) {}!'.format(name))
    print('1. Criar Nova conta.   3. Ver contas.')
    print('2. Ver IMC já criado.  4. Encerrar e sair.')
    lobby = int(input('Escolha entre uma das opções acima: '))
    print()
    if lobby == 1:
        cont =+ 1
        nome = input('Qual o nome da pessoa que está efetuando este IMC? ')
        peso = float(input('Quanto você pesa? '))
        altura = float(input('Qual sua altura? '))
        imc = peso / (altura**2)
        if imc < 18.5:
            sit = 'Abaixo do Peso.'
        elif imc >= 18.5 and imc < 24.9:
            sit = 'Peso Normal.'
        elif imc >= 25 and imc < 29.9:
            sit = 'Sobrepeso.'
        elif imc >= 30 and imc < 34.9:
            sit = 'Obesidade Grau I.'
        elif imc >= 35 and imc < 39.9:
            sit = 'Obesidade Grau II.'
        elif  imc > 40:
            sit = 'Obesidade Grau III.'
        print()
        print('Nome do Cliente:',nome)
        print('Grau de IMC: {:.1f}'.format(imc))
        print('Situação Corpórea:',sit)
        print()
        perg = input('Deseja voltar para a tela inicial? (s/n)')
        if perg == 's':
            print()
            menu()
        else:
            print()
            finished()        
    elif lobby == 2:
        print('2')
    elif lobby == 3:
        print('3')
    elif lobby == 4:
        finished()
    else:
        print('Número não cadastrado.')
    
menu()
