#resoluçao ex 1)
"""Escreva um programa que pede ao utilizador um número inteiro e trata
erros de entrada."""

try:
    numero = int(input("Digite um número inteiro: "))
    print("Número inserido:", numero)
except ValueError:
    print("Erro: O valor deve ser um número inteiro.")
    
    
#resoluçao ex 2)
"""Peça dois números ao utilizador e trate a divisão por zero."""

try:
    a = int(input("Digite o numerador: "))
    b = int(input("Digite o denominador: "))
    print("Resultado da divisão:", a / b)
except ZeroDivisionError:
    print("Erro: Não é possível dividir por zero.")
except ValueError:
    print("Erro: Apenas números inteiros são permitidos.")

 
#resolução ex 3)
"""Verifique se um ficheiro existe antes de o abrir."""

import os
try:
    caminho = input("Digite o caminho do ficheiro: ")
    if os.path.exists(caminho):
        with open(caminho, "r") as ficheiro:
            print(ficheiro.read())
    else:
        print("Erro: O ficheiro não foi encontrado.")
except Exception as e:
    print("Erro inesperado:", e)
    
    
#resolução ex 4)
"""Crie um programa que captura qualquer erro e exibe uma mensagem
apropriada."""

import sys
try:
    numero = int(input("Digite um número: "))
    print("O dobro do número é:", numero * 2)
except Exception as e:
    print("Erro inesperado:", e)
    sys.exit(1)
    
    
#resolução ex 5)    
""" Elabora uma script em python que peça ao utilizador um número e some todos
os números de 1 até esse mesmo número. Deves utilizar o tratamento de
erros."""

try:
    y=0
    numero= int (input ("Intruduza um numero inteiro "))
    for i in range(1,numero+1):
        y+=i
    print(y)
except ValueError:
    print("Erro: Digite apenas números inteiros.")
 
    
""" 6) Elabora uma script em python que peça ao utilizador dois números e devolva
a divisão do primeiro número introduzido pelo seguinte. Trate erros como
divisão por zero e valores inválidos"""
#resolução ex 6)

try:
    numero1= float (input ("Intruduza 1 de 2 numeros "))
    numero2= float (input ("Intruduza 2 de 2 numeros "))
    divisao=numero1/numero2
    print (divisao)
except ValueError:
    print("Erro: Digite um número inteiro válido.")
except ZeroDivisionError:
    print("Erro: Não é possível dividir por zero.")
    
    
    

