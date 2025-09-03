def soma(n1, n2):
    return n1 + n2
def menos(n1, n2):
    return n1 - n2
def vezes(n1, n2):
    return n1 * n2
def dividir(n1, n2):
    if n2 == 0:
        return'Error ao dividir pro 0!'
    else:
        return n1 / n2

opçoes = {
    '1': soma,
    '2': menos,
    '3': vezes,
    '4': dividir,
    '5': exit
}

def menu():
    while True:
        n1 = int(input('Digite um numero: '))
        n2 = int(input('Digite outro numero: '))

        print('Opçoes de calculo: \n1: Somar \n2: Subtrair \n3: Multiplicar \n4: Dividir \n5: Sair')
        resp = int(input('Informe a opçao desejada: '))

        op = input('')
        if op in opçoes.keys():
            print(opçoes[op](n1, n2))
        else:
            print('OPÇAO INVALIDA. Tente novamente')

if __name__== '__main__':
    menu()