"""4. Escreve uma função em Python que dada uma palavra retorne o número de
vogais nessa palavra."""

def contar_vogais(palavra):
    vogais = "aeiouAEIOU"
    contador = 0
    for letra in palavra:
        if letra in vogais:
            contador += 1

    return contador

palavra = input("Digite uma palavra: ")
print(f'Número de vogais: {contar_vogais(palavra)}')