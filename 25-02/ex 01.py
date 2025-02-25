"""1. Escreva um programa que, dada uma sequência de números inteiros
(todos fornecidos na mesma linha, separados por espaços), imprima
a média desses números."""

seq = input(" Entre com uma sequência de varios números: ")
numeros = seq. split()
soma = 0

for n in numeros:
    soma = soma + int(n)
média = soma / len(numeros)

print ("A média dos valores intrduzidos é: ", format(média , ".3f"))