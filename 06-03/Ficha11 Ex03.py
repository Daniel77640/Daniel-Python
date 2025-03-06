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
