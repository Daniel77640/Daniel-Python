"""Reescreve o programa anterior de forma a apresentar a tabuada de qualquer número
introduzido pelo utilizador."""


j= int(input("Intruduza a tabuada pretendida "))
for i in range (1, 11, 1):
    multiplicação= i * j
    print (f"{j} * {i} = {multiplicação}")
    
    
    
#resolução2
while True:
    try:
        num = int(input("Digite um número: "))
        break
    except ValueError:
        print("Entrada inválida. Digite um número inteiro.")

for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")