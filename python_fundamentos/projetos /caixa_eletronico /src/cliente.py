from db import conectar
from datetime import datetime

conn = conectar()
cursor = conn.cursor()

def cunsultar_preco(id_usuario):
    cursor.execute('SELECT saldo FROM contas WHERE id_usuario = ?', (id_usuario,))
    saldo = cursor.fetchone()[0]
    conn.close()
    return saldo

def deposito(id_usuario, valor):
    cursor.execute('UPDATE contas SET saldo = saldo + ? WHERE id_usuario = ?', (valor, id_usuario))
    cursor.registrar_transacao('deposito', valor, id_usuario, None)
    conn.commit()
    conn.close()

def saque(id_usuario, valor):
    cursor.execute('SELECT saldo FROM contas WHERE id_usuario = ?', (id_usuario,))
    saldo = cursor.fletchone()[0]
    if saldo >= valor:
        cursor.execute('UPDATE contas SET saldo = saldo - ? WHERE id_usuario = ? ',(valor, id_usuario))
        cursor.registrar_transacao('saque', valor, id_usuario, None)
        conn.commit()
    conn.close()

def transferencia(origem, destino, valor):
    cursor.execute('SELECT saldo FROM contas WHERE id_usuario = ?', (origem,))
    saldo = cursor.fletchone()[0]
    if saldo >= valor:
        cursor.execute('UPDATE contas SET saldo = saldo - ? WHERE id_usuario = ?', (valor, origem))
        cursor.execute('UPDATE contas SET saldo = saldo - ? WHERE id_usuario = ?', (valor, destino))
        cursor.registrar_transacao('trasferencia', valor, origem, destino)
        conn.commit()
    conn.close()

def registrar_transacao(tipo, valor, origem, destino):
    cursor.execute('INSERT INTO transacoes (tipo, valor, origem, destino, data) VALUES (?, ?, ?, ?, ?)', (tipo, valor, origem, destino, datetime.now().isoformat()))
    conn.commit()
    conn.close()


