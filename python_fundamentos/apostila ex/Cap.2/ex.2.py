# Escreva um script em python que represente uma quitanda. O seu programa deverá
# apresentar as opções de frutas, e a cada vez que você escolher a fruta desejada, a fruta
# deverá ser adicionada a uma cesta de compras.

# MENU PRINCIPAL:
# Quitanda:
# 1: Ver cesta
# 2: Adicionar frutas
# 3: Sair
# Digite a opção desejada:

# MENU DE FRUTAS:
# Escolha fruta desejada:
# 1 - Banana
# 2 - Melancia
# 3 - Morango

# Digite à opção desejada: 2
# Melancia adicionada com sucesso!

cesta = []

while True:
    print('QUITANDA:\n 1: Ver cesta\n 2: Adicionar frutas\n 3: Sair')
    resp = int(input('Digite a opção desejada: '))
    if resp == 1:
        print(cesta)
    elif resp == 2:
        print('MENU DE FRUTAS:\n 1 - Banana\n 2 - Melancia\n 3 - Morango')
        escolha = int(input('Digite a opção desejada: '))
        frutas = {1: 'Banana', 2: 'Melancia', 3: 'Morango'}
        fruta = frutas.get(escolha)
        if fruta:
            cesta.append(fruta)
            print(f'{fruta} adicionada com sucesso!')
        else:
            print(f'Opção invalida')
    elif resp == 3:
        print('Obrigada, volte sempre!')
        break
    else:
        print('OPÇÃO INVALIDA!')
