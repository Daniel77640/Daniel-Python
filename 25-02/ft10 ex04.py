"""a. Imprima o texto anterior todo em maiúsculas;"""

txt="""Python é uma linguagem de programação de 
de alto nível, interpretada de script, imperativa, orientada a objetos,
funcional, de tipagem dinâmica e forte."""

txt=(txt.upper())
print(txt)


"""b. Peça uma palavra ao utilizador e verifique se a mesma está ou não no
texto, devolvendo o resultado ao utilizador."""

palavra=input("Intuduza uma palavra ")
for x in txt:
    if palavra == x:
        print("palavra está no texto")
    else:
        print("palavra não está no texto")
        
        
"""c. Imprima o número de vezes que a letra ‘O’ ocorre no texto"""
x=txt.count("O")
print(x)

"""d. Substitua todas as ocorrências da letra ‘P’ no texto por ‘_’"""
y=txt.replace("P", "_")
print(y)

#resolução
'''4. Considere a seguinte variável:
Txt="""Python é uma linguagem de programação
3 de 3
de alto nível, interpretada de script, imperativa, orientada a objetos,
funcional, de tipagem dinâmica e forte."""
'''
x="""Python é uma linguagem de programação 3 de 3 de alto nível, interpretada de script, imperativa, orientada a objetos, funcional, de tipagem dinâmica e forte."""
#a. Imprima o texto anterior todo em maiúsculas;
print(x.upper())
#c. Imprima o número de vezes que a letra ‘O’ ocorre no texto
print(x.count("o"))
#b. Peça uma palavra ao utilizador e verifique se a mesma está ou não no texto, devolvendo o resultado ao utilizador.
print( input("palavra de pesquisa -") in x)
#d. Substitua todaa as ocorrências da letra ‘P’ no texto por ‘_’
y=x.replace("p","_")
print(y)