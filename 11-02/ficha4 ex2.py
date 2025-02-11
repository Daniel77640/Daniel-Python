"""Implemente um programa que, dada uma letra (S, C ou V), indique o estado civil de
uma pessoa."""

x1 = (input("Indique o seu estado civil (C S V) "))

match x1.upper():
    case "C":
        print ("O seu estado civil corresponde a Casado")
    case "S":
        print ("O seu estado civil corresponde a Solteiro")
    case "V":
        print ("O seu estado civil corresponde a Viuvo")
        
        
#resolução

estado=str(input("Introduza o seu estado civil: S - Solteiro, C - Casado, D - Divorciado, V - Viúvo\n---->\t"))
match estado:
    case "S":
        print("O estado cívil é: Solteiro(a)")
    case "C":
        print("O estado cívil é: Casado(a)")
    case "D":
        print("O estado cívil é: Divorciado(a)")
    case "V":
        print("O estado cívil é: Viúvo(a)")
    case _:
        print("Estado cívil desconhecido")