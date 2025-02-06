""""Escreve um programa que receba três números reais e indique qual o maior dos três
números."""

x = float(input("insere 1 de 3 numeros "))
x1 =float(input("insere 2 de 3 numeros "))
x2 = float(input("insere 3 de 3 numeros "))

if x > x1:
    print ("numero", x "é o maior")
elif x > x2:
    print ("numero", x "é o maior")
elif x1 > x2:
    print ("numero", x1 "é o maior")
elif x1 > x:
    print ("numero", x1 "é o maior")
else
    print ("numero", x2 "é o maior")
    

#resolução1

# Solicita três números reais ao utilizador
numero1 = float(input("Por favor, insira o primeiro número real: "))
numero2 = float(input("Por favor, insira o segundo número real: "))
numero3 = float(input("Por favor, insira o terceiro número real: "))
#1 Encontra o maior número entre os três
maior = numero1   #maior é definido como numero1. ponto de partida para fazer a comparação.
#2 o código verifica se numero2 ou numero3 são maiores que o valor atual de maior. Se for o caso, maior é atualizado para o novo valor mais alto. 
if numero2 > maior:
    maior = numero2
if numero3 > maior:
    maior = numero3
# Imprime o maior número
print(f"O maior número é {maior}.")



    #resolução2    
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))
max = max(num1, num2, num3)
print(f"O maior número é {max}")

