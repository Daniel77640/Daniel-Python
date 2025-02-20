"""3. Efetua um programa em python:"""

#a. Instancie o seguinte dicionário:
Computadores_1={
"Marca":"Asus",
"Ecra":"14Pol",
"RAM": [4, 8, 12]
}

#b. Acrescente um novo elemento à lista com chave igual a “Disco” e valor [“128G”, “256G”]
Computadores_1["disco"] = ["128G ou 256G"]
print (Computadores_1)

#c. Permita ao utilizador introduzir um valor específico de RAM e verificar se esta está presente na lista.
RAM = int (input ("intruduza a RAM pretendida   "))
if RAM == 4 or RAM == 8 or RAM == 12:
    print ("ok")
else: 
    print ("não está presente na lista")
    
#d. Acrecente 16 como novo valor de RAM
Computadores_1.update({"RAM": [4, 8, 12, 16]})
print (Computadores_1)

#e. Copie o dicionário para um novo usando Deep Copy()
cp2 = Computadores_1.copy()
print (cp2)

#No novo dicionário modifique a marca para “Lenovo” e os valores da RAM para [4,8]. Imprima a nova lista
cp2["Marca"] = "Lenovo"
cp2.update({"RAM": [4, 8]})
print (cp2)

#g. Crie uma nova lista com deep copy e modifique a marca para “HP” e Disco para [“256G”]- Imprima a respetiva lista
cp3 = cp2.copy()
cp3["Marca"] =  "HP"
cp3["disco"] =  "256G"
print (cp3)

#h. Cria uma lista cujos elementos são os três dicionários
cp4dic=[]

cp4dic = [Computadores_1, cp2, cp3]
print(cp4dic)

#i. Imprima as marcas com 128G de Disco
if ("disco" == "128G"):
    marca = cp4dic["Marca"]
    print(marca)

#j. Imprima as marcas com 8 e 12 de RAM