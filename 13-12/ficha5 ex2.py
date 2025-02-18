'''Crie um programa para controlar listas, com as seguintes funções:
• Adicionar elemento no início;
• Adicionar elemento no fim;
• Remover elemento;
• Tamanho da lista;
• Imprimir elementos da lista;
• Esvaziar lista;'''

lista=[1,2,3,4,5,6,7,8,9,10,11,12]
lista.insert(0,8)
print(lista) #Adicionar elemento no início;
lista.append(8)
print(lista) #Adicionar elemento no fim;
lista.remove(8)
print(lista) #Remover elemento;
print(len(lista)) #Tamanho da lista;
print(sum(lista)) #Imprimir elementos da lista;
lista.clear()
print(lista) #Esvaziar lista


#resolução2

""""🔹 Exercício 2 - Resolução 2 : Programa para manipular Listas
📌 Enunciado:
Cria um programa para controlar listas, com as seguintes funcionalidades:

Adicionar elemento no início
Adicionar elemento no fim
Remover elemento
Tamanho da lista
Imprimir elementos da lista
Esvaziar lista""""

lista = []

while True:
    print("\n1 - Adicionar elemento no início")
    print("2 - Adicionar elemento no fim")
    print("3 - Remover elemento")
    print("4 - Obter tamanho da lista")
    print("5 - Imprimir elementos da lista")
    print("6 - Esvaziar lista")
    print("7 - Sair")

    opcao = input("Escolha uma opção: ")

    match opcao:
        case "1":
            elemento = input("Digite o elemento a adicionar no início: ")
            lista.insert(0, elemento)

        case "2":
            elemento = input("Digite o elemento a adicionar no fim: ")
            lista.append(elemento)

        case "3":
            if lista:
                elemento = input("Digite o elemento a remover: ")
                if elemento in lista:
                    lista.remove(elemento)
                else:
                    print("Elemento não encontrado.")
            else:
                print("A lista está vazia.")

        case "4":
            print("Tamanho da lista:", len(lista))

        case "5":
            print("Elementos da lista:", lista)

        case "6":
            lista.clear()
            print("A lista foi esvaziada.")

        case "7":
            print("A sair do programa...")
            break

        case _:
            print("Opção inválida, tente novamente.")