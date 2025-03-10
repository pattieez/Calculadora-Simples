while True:
    numero_1 = input('Informe o primeiro número: ')
    numero_2 = input('Informe o segundo número: ')
    operador = input('Informe qual operação deseja fazer.\n(/) - divisão, (*) - múltiplicação, (-) - subtração ou (+) - adição: ')

    numeros_validos = None

    try:
        numero_1 = float(numero_1)
        numero_2 = float(numero_2)
        numeros_validos = True
    except:
        numeros_validos = None
    
    if numeros_validos is None:
        print('Um ou ambos os números digitados são inválidos.')
        continue

    operadores_permitidos = '+*-/'

    if operador not in operadores_permitidos:
        print('Operador inválido.')
        continue

    if len(operador) > 1:
        print('Digite apenas um operador')
        continue

    print('Realizando sua conta. Conira o resultado abaixo: ')
    if operador == '+':
        print(numero_1 + numero_2)
    elif operador == '-':
        print(numero_1 - numero_2)
    elif operador == '/':
        print(numero_1 / numero_2)
    elif operador == '*':
        print(numero_1 * numero_2)
    else:
        print('error')

    sair = input('Quer sair? [s]im: ').lower().startswith('s')
    
    if sair:
        break
    