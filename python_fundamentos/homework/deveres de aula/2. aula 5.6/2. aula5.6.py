menu = {
    1: 'consultar',
    2: 'inserir',
    3: 'deletar',
    4: 'atualizar',
    5: 'exit'
}



while True:
    resp = input('Selecione a opçao desejada:\n 1: Consultar\n '
                 '2: Inserir\n 3: Deletar\n 4: Atualizar\n 5: Exit\n'
                 )

    if resp == '1':
        with open('registro.txt', 'r') as arquivo:
            conteudo = arquivo.read()
        if conteudo == '':
            print('Registro vazio')
        else:
            print(conteudo)

    if resp == '2':
        cpf = input('CPF: ')
        nome = input('Nome: ')
        idade = input('Idade: ')
        sexo = input('Sexo: ')
        uf = input('UF: ')
        with open('registro.txt', 'a') as arquivo:
            registro = (f'\nNome: {nome}\nCPF: {cpf}\nIdade: {idade}\n'
                        f'Sexo: {sexo}\nUF: {uf}\n')
            arquivo.write(registro)


