"""4. Escreve uma função em Python que dada uma palavra retorne o número de
vogais nessa palavra."""

def contar_vogais(palavra):
    vogais = "a", "e", "i", "o", "u", "A", "E", "I", "O", "U"
    contador = 0
    for letra in palavra:
        if letra in vogais:
            contador += 1

    return contador
palavra = input("Digite uma palavra: ")
print(f'Número de vogais: {contar_vogais(palavra)}')

#Resolução 2

'''Escreve uma função em Python que dada uma palavra retorne o número de
vogais nessa palavra.'''
def conta_vogais(palavra):
    vogais = 'aeiou'
    count = 0
    for letra in palavra.lower():
        if letra in vogais:
            count += 1
    return count
print(conta_vogais('palavra')) # 3
print(conta_vogais('cão')) # 2