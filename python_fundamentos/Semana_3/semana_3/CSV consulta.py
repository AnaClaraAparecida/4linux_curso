## Arquivos em formato TXT/CSV

with open('arquivo.csv', 'r') as arquivo:
    cadastro = arquivo.readlines()

# cadastro com readlines é uma lista, cada elemento é
# uma linha o primeiro elemento (indicie 0) da lista
# é o cabeçalho -> cpf(0), nome(1), idade(2), sexo(3),
# uf

# print(cadastro[0].split(',')) # os valores vem como
# string a unica forma de 'desmembrar' ele, é como o slit

# Achar pessoas com UF do RJ
filtro_uf = 'RJ'

for registro in cadastro:
    if registro.split(',')[4] == 'RJ':
        print(registro)

        print('CPF', registro.split(',')[0])
        print('Nome', registro.split(',')[1])
        print('Idade', registro.split(',')[2])
        print('Sexo', registro.split(',')[3])
        print('UF', registro.split(',')[4])

