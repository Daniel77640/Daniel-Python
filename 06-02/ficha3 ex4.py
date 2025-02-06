"""Escreve um programa que receba dois números reais e indique qual o maior dos dois
números. Considera a possibilidade de o utilizador indicar dois números iguais."""

x = float(input("Insere um de 2 numeros inteiros"))
y = float(input("insere segundo de 2 numeros inteiros"))
if x > y:
    print(x, "é maior do que", y)
elif x == y:
    print(x, "é igual", y)
else:
    print(x, "é menor do que", y)
        


#resolução

x = float(input("Digite um número inteiro x:"))
y = float(input("Digite um número inteiro y:"))
if x > y:
    print(x, "é maior do que", y)
elif x == y:
    print(x, "é igual a", y) 
else:
    print(x, "é menor do que", y)
