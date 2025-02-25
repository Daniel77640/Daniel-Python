txt=" uFcd proGRAMação eM pyTHON "
#imprimir o texto
print(txt)

#imprimir o texto sem espaçamento inicial
txt=txt.strip()
print(txt)

#Iprimir frase até à palavra na 13ª posição
print(txt[:13])

#imprimir os ultimos 5 caracterees da frase
print(txt[-5:])

#Imprimir frase em maiusculas
txt=txt.upper()
print(txt)


#formação de strings
nome= "Sandro Oliveira"
print("O {} gosta muito da {}".format(nome, txt))


#alinea g)
print(f"O {nome} gosta muito da {txt}")
