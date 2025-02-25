prov="""o pior cedo é aquele que não quer ver."""

#primeira letra da frase em maiusculas
prov=prov.capitalize()
print(prov)

#separar as palavras da frase onde ocorre espaço e transformar a frase numa lista
palavras=prov.split(" ")
print(palavras)

#Contar a ocurrencia duma palavra numa frase
count=0
for x in palavras:
    if "que" in x:
        count=count+1
print(count)

#substituir uma parte da frase por outra
prov=prov.replace("quer ver", "compra um cão")
print(prov)
