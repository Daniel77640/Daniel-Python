

import sqlite3

def menu():
    while True:
        print("\nMENU DE GESTÃO DE FUNCIONARIOS")
        print("1. Adicionar funcionario")
        print("2. Listar funcionarios")
        print("3. Atualizar salario")
        print("4. Eliminar funcionario")
        print("5. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            nome = input("Nome: ")
            cargo = input("Cargo: ")
            salario = float(input("Salario: "))
            cursor.execute("INSERT INTO funcionarios (nome, cargo, salario) VALUES (?, ?, ?)", (nome, cargo, salario))
            conn.commit()

        elif opcao == '2':
            cursor.execute("SELECT * FROM funcionarios")
            for funcionario in cursor.fetchall():
                print(funcionario)

        elif opcao == '3':
            nome = input("Nome do funcionario: ")
            novo_salario = float(input("Novo salario: "))
            cursor.execute("UPDATE funcionarios SET salario = ? WHERE nome = ?", (novo_salario, nome))
            conn.commit()

        elif opcao == '4':
            nome = input("Nome do funcionario a eliminar: ")
            cursor.execute("DELETE FROM funcionarios WHERE nome = ?", (nome,))
            conn.commit()

        elif opcao == '5':
            conn.commit()
            conn.close()
            break
        else:
            print("Opção inválida! Tente novamente.")

conn = sqlite3.connect('empresa.db')
cursor = conn.cursor()

menu()

