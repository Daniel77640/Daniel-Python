"""Implemente uma calculadora simples com as operações aritméticas básicas. O utilizador
deverá especificar a operação desejada (+,-,*,/) e, em seguida, inserir dois valores.
Caso, o utilizador escolha divisão e insira como valor do denominar 0 mostra uma
mensagem personalizada. Para os restantes casos, mostra no ecrã o resultado da
operação desejada."""

x1 = (input("Escolha a operação (+,-,*,/) "))
x2 = float(input("Escolha o valor 1 "))
x3 = float(input("Escolha o valor 2 "))

match x1:
    case "+":
        print ("A soma é igual a:", x2 + x3)
    case "-":
        print ("A subtração é igual a:", x2 - x3)
    case "*":
        print ("A multiplicação é igual a:", x2 * x3)
    case "/":
        if x3 == 0:
            print ("A divisão não é possivel")
        else:
            print ("A divisão é igual a:", x2 / x3)