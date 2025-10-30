import admin
import cliente

print('~' * 15, 'CAIXA ELETRONICO', '~' * 15)

def escolha():
    while True:
        print('Escolha a forma de login')
        print(' 1) Cliente\n 2) Administraçao\n 3) Sair')
        resp = input()
        if resp == '1':
            print(menu_cliente())
        elif resp == '2':
            print(menu_admin())
        elif resp == '3':
            print('Encerrando programa...')
            print('Volte sempre!!')
            break
        else:
            print('Forma de login invalida')


def menu_cliente():
    print('~' * 15, 'MENU CLIENTE', '~' * 15)
    print(' 1) Consultar saldo\n 2) Depositar\n 3) Sacar\n 4) Transferir\n 5) Alterar senha\n 6) Sair')
    resp = input()
    if resp == '1':
        consultar_saudo()

def menu_admin():
    print('1) Criar cliente\n 2) Desbloquear cliente\n 3) Resetar senha\n 4) Sair')

print(menu_cliente())