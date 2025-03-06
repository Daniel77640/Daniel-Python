""""2 - Escreve uma função em Python que, dados a medida do comprimento do lado de
um quadrado imprima os valores do seu perímero e da sua área (area=lado x
lado; perimetro = 4 x lado)"""

lado = float(input("Digite o comprimento do lado do quadrado: "))
def calcular_quadrado(lado):
    area=lado * lado 
    perimetro=4 * lado 
    
    print(f'A área do quadrado é: {area}')
    print(f'O perímetro do quadrado é: {perimetro}')

calcular_quadrado(lado)


#Resolução 2
def calcular_quadrado(lado):
    area = (lado * lado)
    perimetro = (4 * lado)
    print(f"Os valores do perimetro são {perimetro}")
    print(f"Os valores da area são {area}")
a = int(input("Insira uma medida: "))
calcular_quadrado(a)

#Resolução 3
def areaeperimetoquadrado(lado):
    area = lado*lado
    perimetro = 4*lado
    return area, perimetro

#Resolução 4
l1 = float(input("Introduza o valor do lado"))
    
a1, p1 = areaeperimetoquadrado(l1)
print("area = ", a1, " perimetro =",p1)