"""1. Leia uma cadeia de caracteres no formato “DD/MM/AAAA” e copie o dia, mês e ano para
três variáveis inteiras."""
"""data = input("Digite uma data no seguinte formato DD-MM-AAAA ")
dia, mês, ano = map(int, data.split('-'))
print(f"Dia: {dia}")
print(f"Mês: {mês}")
print(f"Ano: {ano}")"""


"""2. Escreve uma função em Python que dada uma palavra retorne o número de vogais nessa
palavra."""
""""def conta_vogais(serie):
    vogais = "a, e, i, o, u, A, E, I, O, U"
    contador = sum(1 for letra in serie if letra in vogais)
    return contador
serie = input("Digite uma palavra: ")
print(f"O número de vogais é: {conta_vogais(serie)}")"""


"""3. Escreve uma função em Python que dada uma lista de números imprime a soma dos
valores dessa lista, o número de elementos da lista e a media desses valores. Implementa
tratamento de exceções no teu código (try…except…else..finally)."""
"""def analisar_lista():
    try:
        entrada = input("Digite uma lista de números separados por espaço entre eles: ")
        numeros = list(map(float, entrada.split()))
        if not numeros:
            raise ValueError("Lista sem valores. Não sendo possível calcular a média.")
        soma = sum(numeros)
        quantidade = len(numeros)
        media = soma / quantidade
    except ValueError as ve:
        print(f"Erro: {ve}")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")
    else:
        print(f"Soma de valores: {soma}")
        print(f"Número de elementos: {quantidade}")
        print(f"Média de valores: {media:.2f}")
    finally:
        print("Fim dos cálculos.")
analisar_lista()"""


"""4.a. Cria um array de números 1 com shape (8, 2)"""
import numpy as np
"""array = np.ones((8, 2))
print(array)"""


"""4.b. Cria um array de zeros com shape (5, 7)"""
"""array = np.zeros((5, 7))
print(array)"""


"""4.c. Subtraia o novo array de outro com dados aleatórios e armazene-o numa variável
chamada subarray"""
"""array_zeros = np.zeros((5, 7))
array_random = np.random.rand(5, 7)
subarray = array_random - array_zeros
print("Array aleatório:")
print(array_random)
print("\n Array de zeros:")
print(array_zeros)
print("\n Resultado da subtração (subarray):")
print(subarray)"""


"""4.d. Calcula a média dos valores do array subarray"""
array_random = np.random.rand(5, 7)
array_zeros = np.zeros((5, 7))
subarray = array_random - array_zeros
media_subarray = np.mean(subarray)
print("Subarray:")
print(subarray)
print("\n Média dos valores do subarray:", media_subarray)


