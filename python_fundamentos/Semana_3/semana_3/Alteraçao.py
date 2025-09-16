## Arquivos em formato TXT/CSV

with open('arquivo.csv', 'r') as arquivo:
    cadastro = arquivo.readlines()

# cadastro com readlines é uma lista, cada elemento é
# uma linha o primeiro elemento (indicie 0) da lista
# é o cabeçalho -> cpf(0), nome(1), idade(2), sexo(3),
# uf

cpf = '1324'
#for registro in cadastro:
    #if registro .split(',')[0] == cpf:
for indice in range(len(cadastro)):
    if cadastro[indice].split(',')[0] == cpf:
        print(cadastro[indice])
        # remoçao
        del cadastro[indice]
        break

        #alteraçao do cadastro
        #cpf = input('CPF: ')
        #idade = input('Idade: ')
        #sexo = input('Sexo: ')
        #uf = input('UF: ')
        #del cadastro[indice]
        #cadastro[indice] = f'{cpf}, {nome}, {idade}, {sexo}, {uf}\n'

#cadastro.append(registro)
#with open('cadastro.csv', 'w') as arquivo:
    #arquivo.writelines(cadastro)
with open('arquivo.csv', 'w') as arquivo:
    arquivo.writelines(cadastro)

# formato do registro: '1111,Julio,36,M,SP\n'