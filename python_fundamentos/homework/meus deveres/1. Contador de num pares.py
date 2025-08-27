# Crie um programa que peça ao usuário um número inteiro positivo e exiba todos os números pares de 0 até esse número

print('Contador de números pares ')

num = int(input('Digite um numero: '))
if num <= 0:
    print('ERRO! Digite um numero inteiro, que seja maior que 0')

for par in range(0, num):
    if par % 2 == 0:
        print(f'{par}', end=' ')

