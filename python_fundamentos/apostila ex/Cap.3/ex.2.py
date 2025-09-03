# Escreva uma calculadora utilizando funções anônimas

print('-' * 12)
print('CALCULADORA')
print('-' * 12)

calculadora = {
    'soma': lambda x, y: x + y,
    'sub': lambda x, y: x - y,
    'multi': lambda x, y: x * y,
    'divisao': lambda x, y: 'opçao invalida' if y == 0 else x / y,
}

while True:
    n1 = int(input('n1: '))
    n2 = int(input('n2: '))

    print('Opçoes de calculo: \n1: Somar \n2: Subtrair \n3: Multiplicar \n4: Dividir \n5: Sair')
    resp = int(input('Informe a opçao desejada: '))

    if resp == 1:
        print('soma:', calculadora['soma'](n1, n2))
    elif resp == 2:
        print('Subtração:', calculadora['sub'](n1, n2))
    elif resp == 3:
        print('Multiplicação:', calculadora['multi'](n1, n2))
    elif resp == 4:
        print('Divisão:', calculadora['divisao'](n1, n2))
    elif resp == 5:
        print('Encerrando programa...')
        break
    else:
        print('OPÇAO INVALIDA. Tente novamente')


    sn = str(input('Deseja continuar? [S/N]: ')).upper().strip()
    if sn == 'S':
        continue
    elif sn == 'N':
        print('Encerrando programa...')
        break


