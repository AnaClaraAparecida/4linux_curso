dic = {
    '1': lambda x,y : x + y,
    '2': lambda x,y : x - y,
    '3': lambda x,y : x * y,
    '4': lambda x,y : x / y,
    '5': lambda x,y : exit(),
}

while True:
    try: # bloco com potencial travamento (chance de erro)
        n1 = float(input('n1: '))
        n2 = float(input('n2: '))
        res = dic[op](n1, n1)

        op = input(f'Digite a opçao desejada\n'
                   f'1-) Soma \n'
                   f'2-) Subtraçao \n'
                   f'3-) Multiplicaçao \n'
                   f'4-) Divisao \n'
                   f'5-) Sair \n')

    except ZeroDivisionError:
        print('Erro ao dividir por zero')

    except KeyError:
        print('Digite uma opçao valida')

    except ValueError:
        print('Digite apenas numeros')

    except Exception as err:
        print('Erro desconhecido', err)
        # log

    else:
        # proxima instruçao caso for bem sucedido
        print(res)

    finally:
        print('passei por aqui')
    # proxima instruçao