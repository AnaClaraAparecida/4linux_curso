from db import conectar

def criar_cliente(nome, senha):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO usuarios (nome, senha, papel) VALUES (?, ?, "cliente")', (nome, senha))
    user_id = cursor.lastrowid
    cursor.execute('INSERT INTO contas (id_usuario) VALUES (?)', (user_id,))
    conn.commit()
    conn.close()

def desbloquear_usuario(nome):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('UPDATE usuarios SET bloqueado = 0, senha_temporaria = 1 WHERE nome = ?', (nome,))
    conn.commit()
    conn.close()

def resetar_senha(nome, nova_senha):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('UPDATE usuarios SET senha = ?, senha_temporaria = 1 WHERE nome = ?', (nova_senha, nome))
    conn.commit()
    conn.close()

