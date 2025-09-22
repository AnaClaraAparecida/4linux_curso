# 4) Implemente uma função de exclusão no programa do exercício 2.

registro = 'registro.csv'

opc = input('Opçoes de cadastro:\n 1) Cadastrar\n 2) Deletar cadastro\n 3) Pessoas cadastradas (apenas com senha)\n 4) Sair\n')

while True:
    if opc == '1':
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
    elif opc == '2':
        del_cpf = input('Informe o CPF que deseja deletar: ')

    elif opc == '3':
        senha = input('Digitar senha: ')
        if senha == '014010':
            print('\n---Registro---\n')
            with open(registro, 'r') as arquivo:
                print(arquivo.read())
                break
        else:
            print('Senha invalida!')
            break



