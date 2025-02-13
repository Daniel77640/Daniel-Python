"""Considera a lista:
cores=["amarelo", "azul", "branco", "preto", "verde"]
Cria um programa, em python, que:
a. Faz o print de toda a lista
b. Faz o print do indíce 2 da lista
c. Altera o indíce 0 da lista para "vermelho"
d. Faz o print de toda a lista
e. Acrescenta no final da lista a cor "amarelo"
f. Faz o print de toda a lista
g. Acrescenta no indíce 2 a cor "roxo"
h. Faz o print de toda a lista
i. Apaga o último elemento da lista
j. Faz o print de toda a lista
k. Faz o print do tamanho da lista (len)"""

cores=["amarelo", "azul", "branco", "preto", "verde"]

print (cores)
print(cores[2])
cores[0]="vermelho"
print (cores)
cores.append("amarelo")
print (cores)
cores.insert(2, "roxo")
print (cores)
cores.pop()
print (cores)
print(len(cores))
