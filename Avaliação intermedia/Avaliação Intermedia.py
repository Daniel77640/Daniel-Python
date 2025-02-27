import sqlite3
conn = sqlite3.connect("empresa.db")
cursor = conn.cursor()

cursor.execute("INSERT INTO funcionarios (nome, cardgo, salario) VALUES ("Ana Silva", "Gestora", "3500")")
cursor.execute("INSERT INTO funcionarios (nome, cardgo, salario) VALUES ("Pedro Santos", "Programador", "1500")")
cursor.execute("INSERT INTO funcionarios (nome, cardgo, salario) VALUES ("MAriana Costa", "Designer", "3000")")
