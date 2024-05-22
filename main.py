while True:
        
    x = str(input('informe o primeiro numero')).replace(',','.')
    y = str(input('informe o segundo numero')).replace(',','.')

    x = float(x)
    y = float(y)

    print('operações disponíveis.\n')
    print('"+" para somar.')
    print('"-" para subtrair.')
    print('"*" para multiplicar.')
    print('"/" para dividir.')
    print('"%" para encontrar o resto da divisão.')
    

    op = input('operação desejada. ')

    match op:
        case '+':
            print(f'A soma é: (x + y).')
        case '-':
            print(f'A subtração é: (x + y).')
        case '*':
            print(f'A multiplicação é: (x + y).')
        case '/':
            print(f'A divisão é: (x + y).')
        case '%':
            print(f'O resto da divisão é: (x + y).')
        case '_':
            print(f'Operação inválida: (x + y).')
