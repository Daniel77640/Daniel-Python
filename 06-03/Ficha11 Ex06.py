"""6. Escreve uma função que, dado o número do mês retorne o mesmo, por extenso."""

def mes_por_extenso(numero_mes):
    meses = {
        1: "Janeiro",
        2: "Fevereiro",
        3: "Março",
        4: "Abril",
        5: "Maio",
        6: "Junho",
        7: "Julho",
        8: "Agosto",
        9: "Setembro",
        10: "Outubro",
        11: "Novembro",
        12: "Dezembro"
    }
    
    if 1 <= numero_mes <= 12:
        return meses[numero_mes]
    else:
        return "Mês inválido"

numero = int(input("Digite o número do mês (1 a 12): "))
print("Mês por extenso:", mes_por_extenso(numero))


#Resolução 2
x1 = (input("Indique o numero do mes do ano "))

match x1:
    case "1":
        print ("Corresponde ao mês - Janeiro")
    case "2":
        print ("Corresponde ao mês - Fevereiro")
    case "3":
        print ("Corresponde ao mês - Março")
    case "4":
        print ("Corresponde ao mês - Abril")
    case "5":
        print ("Corresponde ao mês - Maio")
    case "6":
        print ("Corresponde ao mês - Junho")
    case "7":
        print ("Corresponde ao mês - Julho")
    case "8":
        print ("Corresponde ao mês - Agosto")
    case "9":
        print ("Corresponde ao mês - Setembro")
    case "10":
        print ("Corresponde ao mês - Outubro")
    case "11":
        print ("Corresponde ao mês - Novembro")
    case "12":
        print ("Corresponde ao mês - Dezembro")
