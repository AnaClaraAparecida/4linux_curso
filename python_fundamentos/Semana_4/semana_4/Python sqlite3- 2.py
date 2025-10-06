import sqlite3

conn = sqlite3.connect('cafe.db')
cursor = conn.cursor()

nome = 'agua'
descricao = 'solvente'
tipo = 'liquido'
unidade_medida = 'ml'

# 3: criar instruçoes SQL
cursor.execute(f"""
    INSERT INTO ingrediente(nome, descricao, tipo, unidade_medida)
    VALUES('{nome}', '{descricao}', '{tipo}', '{unidade_medida}'); 
    
""")

conn.commit()