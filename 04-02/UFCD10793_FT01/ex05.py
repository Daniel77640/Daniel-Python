"""Sejam a e b os catetos de um triângulo retângulo, faz um programa que devolva o valor
da hipotenusa"""

import math
math.sqrt

adj=float (input("Intruduza um numero do cateto a "))

ops=float (input("intruduza um numero do cateto b "))

hipotenusa = math.sqrt(adj**2 + ops**2)

print ("A Hipotenusa é", hipotenusa)

#resolução

import math
print("Programa para calcular o valor da hipotenusa de um triangulo-rectangulo")
adjacente=input("Introduza o comprimento do cateto adjacente:")
adjacente=float(adjacente)
oposto=input("Introduza o comprimento do cateto oposto:")
oposto=float(oposto)

hipotenusa= math.sqrt(adjacente**2 + oposto**2)
print(f"o comprimento da hipotenusa deste triangulo-rectangulo é:{hipotenusa}")


