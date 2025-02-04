numero = input("Intruduza um numero inteiro:\n-->\t ")
numero = int(numero)
dobro = 2*numero

output = "O dobro de %s é %s"(numero,dobro)

output2 = "O dobro de {} é {}".format(numero,2*numero)

output3 = f"O dobro de {numero} é {dobro}"

print(output2)