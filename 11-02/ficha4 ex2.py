"""Implemente um programa que, dada uma letra (S, C ou V), indique o estado civil de
uma pessoa."""

x1 = (input("Indique o seu estado civil (C S V) "))

match x1:
    case "C":
        print ("O seu estado civil corresponde a Casado")
    case "S":
        print ("O seu estado civil corresponde a Solteiro")
    case "V":
        print ("O seu estado civil corresponde a Viuvo")