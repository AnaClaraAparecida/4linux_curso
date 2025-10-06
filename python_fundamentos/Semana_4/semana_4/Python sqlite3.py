import sqlite3

# 1: conectar com o arquivo de banco de dados
conn = sqlite3.connect('cafe.db')

# 2: criar um cursor para executar intruçoes no banco
cursor = conn.cursor()

# 3: criar instruçoes SQL
cursor.execute("""
    CREATE TABLE IF NOT EXISTS ingrediente (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT,
    descricao TEXT,
    tipo TEXT,
    unidade_medida TEXT
);
""")

conn.commit()
conn.close()

