"""Considera a lista
idades=[25, 15, 19, 22, 37, 78, 46, 2, 67]
Cria um programa, em python, que:
a. Indique quantas pessoas são menores de idade
b. Ordene a lista por ordem decrescente
c. Pede ao utilizador uma idade e verifica se essa idade está na lista.
#- Se estiver faz print("A idade está na lista")
#- Caso contrário faz o print("não existe ninguém com essa idade na lista")"""

idades=[25, 15, 19, 22, 37, 78, 46, 2, 67]

x=0
for idade in idades:
    if idade <18:
        x+=1
print(x)

    
idades.sort(reverse = True)
print (idades)


x1= int(input ("indique uma idade "))
if x1 in idades:
    print ("A idade está na lista")
else:
    print("não existe ninguém com essa idade na lista")


