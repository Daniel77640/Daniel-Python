"""O Índice de Massa Corporal (IMC) é utilizado para medir o peso ideal de uma pessoa.
Escreve um programa que peça o nome, a idade, o peso e a altura do utilizado e que,
de seguida, calcule e mostre o resultado do seu IMC e classifique esse resultado de
acordo com as seguintes condições:"""

x1 = (input("Intruduza o nome "))
x2 = float(input("Intruduza a idade "))
x3 = float(input("Intruduza o peso "))
x4 = float(input("Intruduza a altura "))

imc = x3 / (x4 * x4)

if imc < 17:
    print ("Muito baixo do peso ideal")
elif imc >= 17 and imc < 18.5:
    print ("Abaixo do peso")
elif imc >= 18.5 and imc < 25:
    print ("Peso ideal")
elif imc >= 25 and imc < 30:
    print ("Acima do peso")
elif imc >= 30 and imc < 35:
    print ("Obesidade I")
elif imc >= 35 and imc < 30:
    print ("Obesidade II (severa)")
else:
    print ("Obesidade III (móbida)")
 
 
    
#resultado

nome = input("Digite o seu nome: ")
idade = input("Digite a sua idade: ")
peso = float(input("Digite o seu peso: "))
altura = float(input("Digite a sua altura: "))
IMC = round(peso / (altura * altura), 2)
if IMC < 17:
    
    print(f"{nome} seu IMC é {IMC} você está muito abaixo do peso ideal!")
elif IMC >= 17 and IMC < 18.5:
    print(f"{nome} seu IMC é {IMC} você está abaixo do peso!")
    
elif IMC >= 18.5 and IMC < 25:
    print(f"{nome} seu IMC é {IMC} você está no peso normal!")
    
elif IMC >= 25 and IMC < 30:
    
    print(f"{nome} seu IMC é {IMC} você está acima do peso!")
    
elif IMC >= 30 and IMC < 35:
    
    print(f"{nome} seu IMC é {IMC} você está em obesidade I!")
elif IMC >= 35 and IMC < 40:
    
    print(f"{nome} seu IMC é {IMC} você está em obesidade II (severa)!")
    
else:
    
    print(f"{nome} seu IMC é {IMC} você está em obesidade III (mórbida)!")
