"""Escreve um programa que coloque no ecrã a tabuada do número 5"""

for i in range (1, 11, 1):
    j = 5
    multiplicação= i * j
    print (f"{j} * {i} = {multiplicação}")



#resolução

'''Escreve um programa que coloque no ecrã a tabuada do número 5.'''

print("\nTabuada do número 5:")
numero1 = 1
tabuada = 5
multiplicacao = 5
while numero1 <= 10:
    
    multiplicacao = tabuada * numero1 
    print(f"{tabuada} x {numero1} = {multiplicacao}")
    numero1 = numero1 + 1
    
#resolução

i=1
while i<=10:
     print(f"{i} x 5\t {i*5}")
     i=i+1