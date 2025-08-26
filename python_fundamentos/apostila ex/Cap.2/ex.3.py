# Aproveitando o exercício anterior, incremente a sua quitanda para consolidar o valor
# total de sua cesta de compras. Deverá ser adicionado ao seu menu inicial a opção
# checkout e esta deverá listar os produtos de sua cesta bem como o valor total:

# Considere os seguintes preços:
# Banana: 3.50 Melancia: 7.50 Morango: 5.00
# Dica: Você pode armazenar os dados de frutas e seus respectivos preços em um dicionário.



cesta = []
preços = {
    'Banana': 3.50,
    'Melancia': 7.00,
    'Morango': 5.25
}

while True:
    print('QUITANDA:\n 1: Ver cesta\n 2: Adicionar frutas\n 3: Checkout\n 4: Sair')
    resp = int(input('Digite a opção desejada: '))
    if resp == 1:
        if cesta:
            print(cesta)
        else:
            print('Sua cesta esta vazia ):')

# -> nesse caso a funçao get() busca no dicionario a chave para o numero solicitado
# na variavel escolha, e troca as informacoes correnpondentes pela chave desejada
# que no caso é a fruta
# -> no caso do if, a fruta qeu passou pelo processo anterior, é colocada na lista cesta,
# com o append, e o else informa caso a opçao digitada anteriormente esta valida ou nao

    elif resp == 2:
        print('MENU DE FRUTAS:\n 1 - Banana\n 2 - Melancia\n 3 - Morango')
        escolha = int(input('Digite a opção desejada: '))
        frutas = {1: 'Banana' , 2: 'Melancia', 3: 'Morango'}
        fruta = frutas.get(escolha)
        if fruta:
            cesta.append(fruta)
            print(f'{fruta} adicionada com sucesso!')
        else:
            print('Opção invalida')

    elif resp == 3:
        print('CHECKOUT: ')

        # -> caso tiver fruta na cesta ele executa, caso nao, pula pro else
        if cesta:
            # -> somar o valor das frutas
            total = 0
            for fruta in cesta:
                # -> acessa o valor da variavel fruta, e associa ao preço, []
                # acessa uma chave dentro de um dicionario
                valor = preços[fruta]
                print(f'{fruta}: R$ {valor: .2f}')
                total += valor
                print(f'O total da compra foi de: R$ {total: .2f}')


    elif resp == 4:
        final = str(input('Deseja cancelar a sua compra? [S/N]: '))
        if final == 'Ss':
            print('Compra cancelada! Obrigada, volte sempre! (:')
            break
        elif final == 'Nn':
            print('Voltanto para o menu da quitanda...')
            break
        else:
            print('Opçao invalida! Digite [S] ou [N]')
    else:
        print('OPÇÃO INVALIDA!')