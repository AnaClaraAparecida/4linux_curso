# ) Em muitos programas, nos é solicitado o preenchimento de algumas informações como
# nome, CPF, idade e unidade federativa. Escreva um script em Python que solicite as
# informações cadastrais mencionadas e que em seguida as apresente da seguinte forma:

# Confirmação de cadastro:
# Nome: Guido Van Rossum
# CPF: 999.888.777/66
# Idade: 65

print('Confirmação de cadastro:')
nome = input('Digite seu nome: ')
cpf = input('Digite seu CPF: ')
idade = input('Informe a sua idade: ')
print('-' * 30)
print(f'Nome: {nome}\nCPF: {cpf}\nIdade: {idade}')
print('-' * 30)
