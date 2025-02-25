"""Escreva um programa que, dada uma String representando um texto, 
imprima o número de palavras existentes. Observação: você deve
remover os sinais de pontuação (“.”, “,”, “:”, “;”, “!” e“?”) antes
de realizar a contagem das palavras."""

texto = input(" Introduza um texto: ")
pontuacao = [".", ",", ":", ";", "!", "?"]

# remove os sinais de pontuação
for p in pontuacao:
    texto = texto. replace(p, " ")

numpalavras = len(texto. split())
print (" Número de palavras:", numpalavras)