def welcome():
    print("Bem-vindo")
    print('')
welcome()

def calculadora():

    print("Calculadora: \n")

    escolha = input('Menu: \n - : Subtração \n + : Adição \n * : Multiplicação \n / : Divisão \n ** : Petênciação \n Qual a sua escolha? ')
    print('')
    

    numero_1 = float(input("Escolha um número: "))
    numero_2 = float(input("Escolha um número: "))
    print('')
    
    if escolha == '+':
        print(f'{numero_1} + {numero_2} = ')
        print(numero_1 + numero_2)

    elif escolha == '**':
        print(f'{numero_1} ** {numero_2} = ')
        print(numero_1 ** numero_2)

    elif escolha == '/':
        print(f'{numero_1} / {numero_2} = ')
        print(numero_1 / numero_2)

    elif escolha == '-':
        print(f'{numero_1} - {numero_2} = ')
        print(numero_1 - numero_2)

    elif escolha == '*':
        print(f'{numero_1} * {numero_2} = ')
        print(numero_1 * numero_2)

    else:
        print('Você não escolheu uma operação valida, por favor, tente novamente.')
        print('')

    again()

def again():
    calc_again = input('''você quer calcular novamente? \n \n Por favor aperte "S" para "SIM" ou "N" para "NÂO"? ''')

    if calc_again.upper() == 'S':
        calculadora()
    
    elif calc_again.upper() == 'N':
        print('Vejo você depois')

    else:
        again()
opcao = 1 

def imc():

    print('IMC: \n')

    altura = float(input('Digite a sua altura: '))
    peso = float(input('Digite o seu peso: '))

    imc = peso / altura ** 2

    if imc < 16:
        print("\nMagreza grave")

    elif imc < 17:
        print("\nMagreza moderada")

    elif imc < 18.5:
        print("\nMagreza leve")

    elif imc < 25:
        print("\nSaudável")

    elif imc < 30:
        print("\nSobrepeso")

    elif imc < 35:
        print("\nObesidade Grau I")

    elif imc < 40:
        print("\nObesidade Grau II (severa)")

    else:
        print("\nObesidade Grau III (mórbida)")
    again_imc()  

def again_imc():
    imc_again = input('''você quer calcular novamente?\nPor favor aperte "S" para "SIM" ou "N" para "NÂO"? ''')

    if imc_again.upper() == 'S':
        imc()
        
    elif imc_again.upper() == 'N':
        print('Vejo você depois')

    else:
        again_imc()
opcao = 2

def raiz_quadrada():

    print('Raiz Quadrada: \n')

    numero1 = float(input("escolha um numero: "))
    raiz =  float(numero1)**0.5
    print('')

    print(f'\n A raiz quadrada de {numero1} é: {raiz}\n')    

def again_raiz():
    raiz_again = input('''você quer calcular novamente?\nPor favor aperte "S" para "SIM" ou "N" para "NÂO"? ''')
    
    print('')

    if raiz_again.upper() == 'S':
        raiz_quadrada()
        
    elif raiz_again.upper() == 'N':
        print('Vejo você depois')

    else:
        again_imc()
        print('')

opcao = 3

while opcao:
    print('')
    print('\n'"1. Calculadora")
    print("2. IMC")
    print('3. Raiz \n')


    opcao = int(input("Opção: "))
    print('')


    if(opcao == 1):
        calculadora()

    if(opcao == 2):
        imc()

    if(opcao == 3):
        raiz_quadrada()
