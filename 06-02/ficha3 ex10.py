"""Implemente uma calculadora simples com as operações aritméticas básicas. O utilizador
deverá especificar a operação desejada (+,-,*,/) e, em seguida, inserir dois valores.
Caso, o utilizador escolha divisão e insira como valor do denominar 0 mostra uma
mensagem personalizada. Para os restantes casos, mostra no ecrã o resultado da
operação desejada."""

x1 = (input("Escolha a operação (+,-,*,/) "))
x2 = float(input("Escolha o valor 1 "))
x3 = float(input("Escolha o valor 2 "))

if x1 == "+":
    print ("a soma é igual a:", x2 + x3)
elif x1 == "-":
    print ("a subtração é igual a:", x2 - x3)
elif x1 == "*":
    print ("a multiplicação é igual a:", x2 * x3)
else:
    if x3 == 0:
        print ("a divisão não é possivel")
    else:
        print ("a divisão é igual a:", x2 / x3)