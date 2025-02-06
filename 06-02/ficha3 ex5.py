"""Escreva um programa que verifique se um determinado número introduzido pelo
utilizador é nulo, positivo ou negativo."""

x = float(input("Insere um numero inteiro "))

if x > 0:
    print("o numero é positivo")
elif x < 0:
    print("o numero é negativo")
else:
    print("o numero é nulo")
    


#resolução


numero = float(input("Introduza um número: "))

if numero > 0:
    print("O número é positivo.")
elif numero < 0:
    print("O número é negativo.")
else:
    print("O número é nulo.")
