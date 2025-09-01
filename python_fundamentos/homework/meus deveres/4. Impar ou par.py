# Objetivo: Usar lógica dentro de uma função.
# Enunciado: Crie uma função chamada verifica_par(numero) que retorne True se o número for
# par e False se for ímpar. Teste a função com diferentes valores
# e imprima os resultados.

def var_par(n):
    if n % 2 == 0:
        print(True)
    else:
        print(False)
    return n

print('DIGITE UM NUMERO E DESCUBRA SE É PAR OU IMPAR!')
n = int(input('Numero: '))
resp = var_par(n)
print(f'{resp}')