# pasta para conectar ao banco de dados

import sqlite3

def conectar():
    return sqlite3.connect('banco.db')

def criar_tabela():
    conn = conectar() # facilitar a conexao ao banco de dedos
    cursor = conn.cursor()

    # Login de cada perfil
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT, 
        nome TEXT, 
        senha TEXT, 
        papel TEXT, # definir se é cilente ou admin
        bloqueado INTEGER DEFAULT 1, # 1 = block 0 = unblock
        senha_temporaria INTEGER DEFAULT 1 # 1 = trocar a senha 0 = senha definida
    )""")

    # saldo no banco
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS contas (
        id_usuario INTEGER, 
        saldo REAL DEFAULT 0, # valor disponivel 
        FOREIGN KEY(id_usuario) REFERENCES usuarios(id)
    )""")

    # historico de operaçao
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS transacoes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        tipo TEXT, # (deposito, saque, tranferencia)
        valor REAL, 
        origem INTEGER, 
        destino INTEGER, 
        data TEXT
    )""")
    conn.commit()
    conn.close()

