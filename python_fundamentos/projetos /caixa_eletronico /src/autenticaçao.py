from db import conectar

def login(nome, senha):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM usuarios WHERE nome = ?", (nome,))
    user = cursor.fetchone()
    if not user:
        return None, 'Usuario nao encontrado'
    if user[4]: # bloqueado
        return None, 'Usuario bloqueado'
    if user[2] != senha:
        return None, 'Senha incorreta'
    return user, 'login bem-sucedido '
