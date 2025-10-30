from db import conectar
from datetime import datetime

def consultar_saldo(id_usuario):
    conn = conectar()
    cursor = conn.cursor()
    id_usuario = input('Digite o ID do usuario: ')
    print(f'Saldo atual: R${saldo}')
    cursor.execute('SELECT saldo FROM contas WHERE id_usuario = ?', (id_usuario,))
    saldo = cursor.fetchone()[0]
    conn.close()
    return saldo

def deposito(id_usuario, valor):
    conn = conectar()
    try:
        cursor = conn.cursor()
        cursor.execute('UPDATE contas SET saldo = saldo + ? WHERE id_usuario = ?', (valor, id_usuario))
        registrar_transacao(cursor, 'depósito', valor, id_usuario, None)
        conn.commit()
    finally:
        conn.close()

def saque(id_usuario, valor):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('SELECT saldo FROM contas WHERE id_usuario = ?', (id_usuario,))
    saldo = cursor.fetchone()[0]
    if saldo >= valor:
        cursor.execute('UPDATE contas SET saldo = saldo - ? WHERE id_usuario = ? ',(valor, id_usuario))
        registrar_transacao('saque', valor, id_usuario, None)
        conn.commit()
    conn.close()

def transferencia(origem, destino, valor):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('SELECT saldo FROM contas WHERE id_usuario = ?', (origem,))
    saldo = cursor.fletchone()[0]
    if saldo >= valor:
        cursor.execute('UPDATE contas SET saldo = saldo - ? WHERE id_usuario = ?', (valor, origem))
        cursor.execute('UPDATE contas SET saldo = saldo + ? WHERE id_usuario = ?', (valor, destino))
        registrar_transacao('trasferencia', valor, origem, destino)
        conn.commit()
    conn.close()

def registrar_transacao(tipo, valor, origem, destino):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO transacoes (tipo, valor, origem, destino, data) VALUES (?, ?, ?, ?, ?)', (tipo, valor, origem, destino, datetime.now().isoformat()))
    conn.commit()
    conn.close()


