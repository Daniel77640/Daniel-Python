"""Escreve um programa para classificar um triângulo de acordo com o comprimento dos
seus lados. Considere as seguintes informações:
• Triângulo equilátero: todos os lados possuem o mesmo comprimento;
• Triângulo escaleno: todos os lados possuem comprimento diferente;
• Triângulo isósceles: caracterizado por ter dois lados com o mesmo comprimento."""

x1 = float(input("Intruduza 1 dos 3 lados do triangulo "))
x2 = float(input("Intruduza 2 dos 3 lados do triangulo "))
x3 = float(input("Intruduza 3 dos 3 lados do triangulo "))
if x1 == x2 == x3:
    print("É um triangulo equilátero")
elif x1 != x2 != x3:
    print("É um triangulo escaleno")
else:
    print("É um triangulo isósceles")
    
    
#resolução
lado_a = float(input("Digite o primeiro lado\n "))
lado_b = float(input("Digite o segundo lado\n "))
lado_c = float(input("Digite o terceiro lado\n "))
if lado_a == lado_b == lado_c:
    print("Triângulo equilátero")
elif lado_a != lado_b != lado_c:
    print("Triângulo escaleno")
else:
    print("Triângulo isósceles")
