print('1 - Soma')
print('2 - Subtração')
print('3 - Multiplicação')
print('4 - Divisão')
print('5 - Sair\n')

op = int(input('Escolha uma operação para fazer: '))
while op != 5:

  if op == 1:
    n1 = int(input('\nDigite um número: '))
    n2 = int(input('Digite outro número: '))

    res = n1 + n2
    print('\nO resultado da soma é: {}\n'.format(res))



    print('1 - Soma')
    print('2 - Subtração')
    print('3 - Multiplicação')
    print('4 - Divisão')
    print('5 - Sair\n')

    op = int(input('Escolha uma operação para fazer: '))

  elif op == 2:
    n1 = int(input('\nDigite um número: '))
    n2 = int(input('Digite outro número: '))

    res = n1 - n2
    print('\nO resultado da subtração é: {}\n'.format(res))

    print('1 - Soma')
    print('2 - Subtração')
    print('3 - Multiplicação')
    print('4 - Divisão')
    print('5 - Sair\n')

    op = int(input('Escolha uma operação para fazer: '))

  elif op == 3:
    n1 = int(input('\nDigite um número: '))
    n2 = int(input('Digite outro número: '))

    res = n1 * n2
    print('\nO resultado da multiplicação é: {}\n'.format(res))

    print('1 - Soma')
    print('2 - Subtração')
    print('3 - Multiplicação')
    print('4 - Divisão')
    print('5 - Sair\n')

    op = int(input('Escolha uma operação para fazer: '))

  elif op == 4:
    n1 = int(input('\nDigite um número: '))
    n2 = int(input('Digite outro número: '))

    res = n1 / n2
    print('\nO resultado da divisão2 é: {:.0f}\n'.format(res))

    print('1 - Soma')
    print('2 - Subtração')
    print('3 - Multiplicação')
    print('4 - Divisão')
    print('5 - Sair\n')

    op = int(input('Escolha uma operação para fazer: '))

  elif op <= 0 or op >= 6:
    print('OPÇÃO INVALIDA!\n')
    print('1 - Soma')
    print('2 - Subtração')
    print('3 - Multiplicação')
    print('4 - Divisão')
    print('5 - Sair\n')

    op = int(input('Escolha uma operação para fazer: '))
    
print('FIM!')