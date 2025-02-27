import sqlite3

conn = sqlite3.connect ("empresa.db")
cursor = conn.cursor()

cursor.execute ("""
CREATE TABLE IF NOT EXISTS funcionarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    cargo TEXT NOT NULL,
    salario TEXT NOT NULL
    )
""")

conn.commit()
conn.close()