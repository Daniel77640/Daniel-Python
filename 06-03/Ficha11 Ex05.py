"""5. Escreve uma função em Python que, dada uma lista de elementos, devolva
essa mesma lista, mas sem elementos repetidos."""

def remover_repetidos():

    entrada = input("Digite os elementos da lista separados por vírgula (podem ser números ou palavras): ")
    

    lista = [elemento.strip() for elemento in entrada.split(',')]
    

    lista_convertida = []
    for elemento in lista:
        try:
            if '.' in elemento:
                lista_convertida.append(float(elemento))
            else:
                lista_convertida.append(int(elemento))
        except ValueError:
            lista_convertida.append(elemento)
    
    lista_unica = []
    for item in lista_convertida:
        if item not in lista_unica:
            lista_unica.append(item)
    
    return lista_unica

resultado = remover_repetidos()
print("Lista sem elementos repetidos:", resultado)


#Resolução2
def ex5(elemento):
    elementos = []
    for p in elemento:
        if p not in elementos:
            elementos.append(p)
    return elementos

import minhasfunc
elemento = input("Escreva uma frase: ")
z = minhasfunc.ex5(elemento)
print(z)

