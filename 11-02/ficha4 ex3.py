""""Fazer um programa para ler quatro números inteiros e positivos, calcular e devolver a sua
média"""

x1 = int(input("Indique 1 de quatro números inteiros e positivos "))
x2 = int(input("Indique 2 de quatro números inteiros e positivos "))
x3 = int(input("Indique 3 de quatro números inteiros e positivos "))
x4 = int(input("Indique 4 de quatro números inteiros e positivos "))

Media = (x1+x2+x3+x4)/4

print ("A media dodos valores é: {Media}")
print (Media)

#Resolução

contador = 1
soma = 0
while contador <=4:
    numero = int(input(f"intruduza o {contador}º numero: "))
    soma += numero
    contador =contador + 1

media = soma / 4
print(f"A media dos numeros intrduzidos é {media}")







contador = 0
soma = 0
while contador <4:
    numero = int(input(f"intruduza o {contador +1}º numero: "))
    soma += numero
    contador =contador + 1
media = soma / 4
print(f"A media dos numeros intrduzidos é {media}")



#opçãp 3
import statistics
contador = 1
lista = []
while contador <=4:
    numero = int(input(f"Introduza o {contador}º número: "))
    lista.append(numero)
    contador =contador + 1
    
media = statistics.mean(lista)
print(lista)
print(f"A média dos números introduzidos é {media}")