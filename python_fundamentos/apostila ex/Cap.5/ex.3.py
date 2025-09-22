# 3) Implemente uma função de consulta no programa do exercício 2.

registro = 'registro.csv'

with open(registro, 'a') as arquivo:
    cpf = input('CPF: ')

    if len(cpf) == 11:
        cpf_format = f'{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}.{cpf[9:]}'
    else:
        print('CPF com numeros invalidos! tente novamente...')
        exit()

    nome = input('Nome: ')
    idade = input('Idade: ')
    sexo = input('Sexo[F/M]: ').strip().upper()
    endereço = input('Endereço: ')

    cadastro = f'\nCPF:{cpf_format}\nNome:{nome}\nIdade:{idade}\nSexo:{sexo}\nEndereço:{endereço}\n'
    arquivo.write(cadastro)

print('Cadastro salvo com sucesso!')

resp = input('Deseja ver os registro?[S/N]: ').strip().upper()

while True:
    if resp == 'S':
        senha = input('Digitar senha: ')
        if senha == '014010':
            print('---Registro---')
            with open(registro, 'r') as arquivo:
                print(arquivo.read())
            break
        else:
            print('Senha invalida!')
    elif resp == 'N':
        print('Encerrando programa...')
        break
    else:
        print('Erro de digitaçao! [S] ou [N]: ')