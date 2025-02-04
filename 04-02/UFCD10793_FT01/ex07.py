distancia=float(input("Distância percorrida(km): "))
combustivel=float(input("Litros de combustível consumidos: "))
consumo=combustivel/distancia*100
print("O consumo do seu veículo é: ",consumo)
print(f"O consumo do seu carro é : {consumo:.2f}")


#resolução
km = input("introduza os km percurridos: ")
litros = input("introduza os litros gastos: ")
kml = (float(km)) / (float(litros))
lkm = (float(litros)) / (float(km))
print("o seu consumo foi ", kml, "Km/l")
print("o seu consumo foi ", lkm, "l/km")


