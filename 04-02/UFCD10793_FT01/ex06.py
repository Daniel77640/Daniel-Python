"""Faz um programa que receba três parâmetros inteiros (horas, minutos e segundos) e
converta o resultado para segundos, devolvendo o output para o ecrã"""

horas=float(input("introduza numero de horas"))
minutos=float(input("introduza numero de minutos"))
segundos=float(input("introduza numero de segundos"))
print(horas*3600+minutos*60+segundos)


#resolução

print("Vou lhe pedir para inserir uma quantidade de horas\n aquantidade de minutos e segundos\n e vou lhe dizer quantos segundos são.\n")
horas = input("Digite a quantidade de horas: ")
minutos = input("Digite a quantidade de minutos: ")
segundos = input("Digite a quantidade de segundos: ")
horas = int(horas)
minutos = int(minutos)
segundos = int(segundos)
segundos = horas * 3600 + minutos * 60 + segundos
output = f"O total de segundos é: {segundos}"
print(output)