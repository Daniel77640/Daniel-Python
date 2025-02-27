import sqlite3

conn = sqlite3.connect ("empresa.db")
cursor = conn.cursor()

cursor.execute ("""
CREATE TABLE IF NOT EXISTS Alunos (
    id INTEGER PRMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    idade INTEGER,
    curso TEXT
    )
""")

conn.commit()
conn.close()