# Reescreva o exercício da quitanda do capítulo 2 separando as operações em funções.

# dados
cesta = []
preços = {
    'Banana': 3.50,
    'Melancia': 7.00,
    'Morango': 5.25
}

# funções
def ver_cesta():
    if cesta:
        print(cesta)
    else:
        print('Sua cesta esta vazia ):')

def add_frutas():
    print('MENU DE FRUTAS:\n 1 - Banana\n 2 - Melancia\n 3 - Morango')
    escolha = int(input('Digite a opção desejada: '))
    frutas = {1: 'Banana', 2: 'Melancia', 3: 'Morango'}
    fruta = frutas.get(escolha)
    if fruta:
        cesta.append(fruta)
        print(f'{fruta} adicionada com sucesso!')
    else:
        print('Opção invalida')

def checkout():
    print('CHECKOUT: ')
    if cesta:
        total = 0
        for fruta in cesta:
            valor = preços[fruta]
            print(f'{fruta}: R$ {valor: .2f}')
            total += valor
            print(f'O total da compra foi de: R$ {total: .2f}')

def sair():
    final = str(input('Deseja cancelar a sua compra? [S/N]: ')).upper().strip()
    if final == 'S':
        print('Compra cancelada! Obrigada, volte sempre! (:')
        return True
    elif final == 'N':
        print('Voltanto para o menu da quitanda...')
        return True
    else:
        print('Opçao invalida! Digite [S] ou [N]')
        return False

# Main()
while True:
    print('QUITANDA:\n 1: Ver cesta\n 2: Adicionar frutas\n 3: Checkout\n 4: Sair')
    resp = int(input('Digite a opção desejada: '))

    if resp == 1:
        ver_cesta()
    elif resp == 2:
        add_frutas()
    elif resp == 3:
        checkout()
    elif resp == 4:
        sair()
        break
    else:
        print('Opção invalida...')