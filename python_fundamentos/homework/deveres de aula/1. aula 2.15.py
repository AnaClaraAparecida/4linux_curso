# Menu interativo que solicite ao usuario dois numeros, tendo as opçes de soma, subtraçao, mutiplicaçao ou divisao

while True:
    n1 = int(input('Digite um numero: '))
    n2 = int(input('Digite outro numero: '))

    print('Opçoes de calculo: \n1: Somar \n2: Subtrair \n3: Multiplicar \n4: Dividir \n5: Sair')
    resp = int(input('Informe a opçao desejada: '))

    if resp == 1:
        soma = n1 + n2
        print(f'{n1} + {n2} = ? \nA soma de {n1} e {n2} é = {soma}')
    elif resp == 2:
        sub = n1 - n2
        print(f'{n1} - {n2} = ? \nA subtraçao de {n1} e {n2} é = {sub}')
    elif resp == 3:
        multi = n1 * n2
        print(f'{n1} X {n2} = ? \nA multiplicaçao de {n1} e {n2} é = {multi}')
    elif resp == 4:
        div = n1 / n2
        if n2 == 0:
            print('Error ao dividir pro 0!')
        else:
            print(f'{n1} / {n2} = ? \nA divisao de {n1} e {n2} é = {div}')
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

print('Programa finalizado! ')