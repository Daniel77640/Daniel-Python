import sqlite3
conn = sqlite3.connect("empresa.db")
cursor = conn.cursor()

cursor.execute("INSERT INTO funcionarios (nome, cargo, salario) VALUES ('Ana Silva', 'Gestora', 3500)")
cursor.execute("INSERT INTO funcionarios (nome, cargo, salario) VALUES ('Pedro Santos', 'Programador', 1500)")
cursor.execute("INSERT INTO funcionarios (nome, cargo, salario) VALUES ('Mariana Costa', 'Designer', 3000)")

conn.commit()
conn.close()

#Acrescentar mais 2 funcionarios

import sqlite3
conn = sqlite3.connect("empresa.db")
cursor = conn.cursor()

cursor.execute("INSERT INTO funcionarios (nome, cargo, salario) VALUES ('Daniel Matos', 'SubBigBoss', 6000)")
cursor.execute("INSERT INTO funcionarios (nome, cargo, salario) VALUES ('Pedro PEreira', 'BigBoss', 2500)")

conn.commit()
conn.close()

cursor.execute("empresa.db")
