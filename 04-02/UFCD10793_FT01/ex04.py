import math
raio = input("Intruduza o raio da esfera ")
raio=float(raio)
math.pi
pi=3.14
volume=round ((4/3)*pi*(raio**3), 2)
print("O volume da esfera é", volume )

RESOLUÇÃO
''' Escreve um programa que calcule o volume de uma esfera. O valor do raio deverá ser 
introduzido pelo utilizador (deverá ser criado o ficheiro ex04.py). '''
import math
pi = math.pi
raio = input ("Introduza um valor para o raio:\n---->\t")
raio = float(raio)
volume = round (4/3*pi*raio**3, 2)
output = f"o volume da esfera com raio {raio} é {volume}" #formated stringd
print (output)