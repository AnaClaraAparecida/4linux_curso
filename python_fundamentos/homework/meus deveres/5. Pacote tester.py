from calculo import *

print('{CALCULADORA}')

n2 = int(input('Digite um valor: '))
n1 = int(input('Digite outro valor: '))

print('Escolha uma das opcoes: ')
print(' 1. Soma\n 2. Multiplicaçao\n 3. Subtraçao\n 4. Divisao')
resp = int(input(' '))

if resp == 1:
    print(soma(n1, n2))
elif resp == 2:
    print(multiplicaçao(n1, n2))
elif resp == 3:
    print(subtraçao(n1, n2))
elif resp == 4:
    print(divisao(n1, n2))
else:
    print('Opçao invalida...')