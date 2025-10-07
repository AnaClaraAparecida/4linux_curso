import sqlite3 
conn = sqlite3.connect('cafe.db')
cursor = conn.cursor()

SQL = """
    UPDATE Ingredientes 
    SET unidade_medida = 'l'
    WHERE id = 1
"""
cursor.execute(SQL)

# VERIFICAR ALTERAÇAO 
