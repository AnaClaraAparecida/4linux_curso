import admin
import cliente

print('~' * 15, 'CAIXA ELETRONICO', '~' * 15)

def escolha():
    print('Escolha a forma de login ')


def menu_cliente():
    print('~' * 15, '', '~' * 15)

    print(' 1) Consultar saldo\n 2) Depositar\n 3) Sacar\n 4) Transferir\n 5) Alterar senha\n 6) Sair')


def menu_admin():
    print('1) Criar cliente\n 2) Desbloquear cliente\n 3) Resetar senha\n 4) Sair')

print(menu_cliente())