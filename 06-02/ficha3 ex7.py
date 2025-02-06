"""Elabora um programa para verificar se um ano é bissexto ou não. A condição para ser
um ano bissexto é: o ano deve ser divisível por 400; ou se for divisível por 4 e não for
divisível por 100."""

x = int(input("intruduza um ano a fim de averiguar se é bisseixto: "))
if x %400 == 0 or (x % 100 != 0 and x % 4 ==0):
    print("O ano", x, "é bisseixto")
else:
    print("O ano" , x, "não é Bissexto")   
    
    
#resolução1
''' Elabora um programa para verificar se um ano é bissexto ou não. A condição para ser
um ano bissexto é: o ano deve ser divisível por 400, ou se for divisível por 4 e não for
divisível por 100.'''

ano = int(input("Introduza um ano a fim de averiguar se é Bissexto:"))
if ano % 400 == 0 or (ano % 100 != 0 and ano % 4 == 0):
    print("O ano" , ano, "é Bissexto")
else:
    print("O ano" , ano, "não é Bissexto")
    
    
#resolução2
ano = input ("Introduza um ano:\n---->\t")
ano = int(ano)
if ano % 400 == 0:
    print(f"{ano} é bissexto")
elif ano%4 == 0 and ano%100 != 0:
    print(f"{ano} é bissexto")
else:
    print(f"{ano} é não é bissexto")
