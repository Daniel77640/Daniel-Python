"""3. Escreve uma função em Python que dada uma lista de números imprime a soma
dos valores dessa lista, o número de elementos da lista e a media desses
valores."""

def analisar_lista(lista):
    soma = sum(lista) 
    num_elementos = len(lista) 
    if num_elementos > 0:
        media = soma / num_elementos 
    else:
        media = 0      
    
    print(f'Soma dos valores: {soma}')
    print(f'Número de elementos: {num_elementos}')
    print(f'Média dos valores: {media}')

lista_numeros = [4, 12, 45, 100, 56, 23, 9]
analisar_lista(lista_numeros)


#Resolução2
def numeros(dados):
    import statistics
    user = list(map(int, dados.split()))
    soma = sum(user)
    conta_numeros = len(user)
    media = statistics.mean(user)
    return soma, conta_numeros, media

#resolução3
import minhasfunc
dados = input("Escreve uma quantidade de números, divididos por espaço: ")
soma, conta_numeros, media = minhasfunc.numeros(dados)
print(f"A soma de todos os números é {soma}; a lista tem {conta_numeros} números e a média é {media}")

#Resolução4
import minhasfunc

valores = [8,9,10]

res = minhasfunc.dadoslista(valores)
print("Sum: ", res[0])
print("Number of items: ", res[1])
print("Average: ", res[2])