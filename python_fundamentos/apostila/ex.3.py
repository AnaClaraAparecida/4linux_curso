# Escreva um script em Python que receba dois números e que seja realizado as seguintes
# operações:
# • soma dos dois números
# • diferença dos dois números
# O resultado deverá ser apresentado conforme a seguir - no exemplo foram digitados os números
# 4 e 2:
# Soma: 4 + 2 = 6
# Diferença: 4 - 2 = 2

num1 = input('Digite um numero: ')
num2 = input('Digite outro numero: ')

soma = int(num1) + int(num2)
sub = int(num1) - int(num2)
print('-' * 15)
print(f'Soma: {num1} + {num2} = {soma}\nDifença: {num1} - {num2} = {sub}')
