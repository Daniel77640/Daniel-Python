x1 = (input("Indique o nome do produto para: A - smartphone B - tablet C - laptop D - outro "))

x2 = float(input("Indique o preço do produto "))

match x1:
    case "A":
        print ("o valor a pagar é:", x2 * 0.90)
    case "B":
        print ("o valor a pagar é:", x2 * 0.85)
    case "C":
        print ("o valor a pagar é:", x2 * 0.80)
    case "D":
        print ("o valor a pagar é:", x2)


#resultado

#Seleccionar o produto e aplicar o desconto
codigo_produto=int(input("introduza o código do produto(Smartphone=1, Tablet=2, laptop=3, Outro=4)"))
preco=float(input("introduza o preço do produto:"))
match codigo_produto:
    case (1):
        preco_final=preco*0.90
        print(f"O preço final é: {preco_final}")
    case (2):
        preco_final=preco*0.85
        print(f"O preço final é: {preco_final}")
    case (3):
        preco_final=preco*0.80
        print(f"O preço final é: {preco_final}")
    case (4):
        preco_final=preco
        print(f"O preço final é: {preco_final}")
    case _:
         print("código inválido")