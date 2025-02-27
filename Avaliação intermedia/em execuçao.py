import sqlite3

conexao = sqlite3.connect("universidade.db")

cursor = conexao.cursor()

cursor.execute ("""
CREATE TABLE IF NOT EXISTS Alunos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    idade INTEGER,
    curso TEXT)
""")


print ("tabela criada com sucesso!")

conexao.commit()
conexao.close()