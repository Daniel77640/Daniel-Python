#resoluçao ex 1)
"""Escreva um programa que pede ao utilizador um número inteiro e trata
erros de entrada."""

try:
    numero = int(input("Digite um número inteiro: "))
    print("Número inserido:", numero)
except ValueError:
    print("Erro: O valor deve ser um número inteiro.")
    
    
#resoluçao ex 2)
"""Peça dois números ao utilizador e trate a divisão por zero."""

try:
    a = int(input("Digite o numerador: "))
    b = int(input("Digite o denominador: "))
    print("Resultado da divisão:", a / b)
except ZeroDivisionError:
    print("Erro: Não é possível dividir por zero.")
except ValueError:
    print("Erro: Apenas números inteiros são permitidos.")

 
#resolução ex 3)
"""Verifique se um ficheiro existe antes de o abrir."""

import os
try:
    caminho = input("Digite o caminho do ficheiro: ")
    if os.path.exists(caminho):
        with open(caminho, "r") as ficheiro:
            print(ficheiro.read())
    else:
        print("Erro: O ficheiro não foi encontrado.")
except Exception as e:
    print("Erro inesperado:", e)
    
    
#resolução ex 4)
"""Crie um programa que captura qualquer erro e exibe uma mensagem
apropriada."""

import sys
try:
    numero = int(input("Digite um número: "))
    print("O dobro do número é:", numero * 2)
except Exception as e:
    print("Erro inesperado:", e)
    sys.exit(1)
    
    
#resolução ex 5)    
""" Elabora uma script em python que peça ao utilizador um número e some todos
os números de 1 até esse mesmo número. Deves utilizar o tratamento de
erros."""

try:
    y=0
    numero= int (input ("Intruduza um numero inteiro "))
    for i in range(1,numero+1):
        y+=i
    print(y)
except ValueError:
    print("Erro: Digite apenas números inteiros.")
 
    
""" 6) Elabora uma script em python que peça ao utilizador dois números e devolva
a divisão do primeiro número introduzido pelo seguinte. Trate erros como
divisão por zero e valores inválidos"""
#resolução ex 6)

try:
    numero1= float (input ("Intruduza 1 de 2 numeros "))
    numero2= float (input ("Intruduza 2 de 2 numeros "))
    divisao=numero1/numero2
    print (divisao)
except ValueError:
    print("Erro: Digite um número inteiro válido.")
except ZeroDivisionError:
    print("Erro: Não é possível dividir por zero.")
    

"""1) Reproduz o seguinte Código que tem como objetivo:
Criar um programa que leia um ficheiro de texto e exibir o seu conteúdo"""
#resolução ex 1)

with open("exemplo.txt", "r") as ficheiro:
    conteudo = ficheiro.read()
    print(conteudo)  
    

""""Reproduz o seguinte Código que tem como objetivo:
Modificar o exercício anterior para exibir o conteúdo linha por linha."""
#resolução ex 2)

with open("exemplo.txt", "r") as ficheiro:
    for linha in ficheiro:
        print(linha.strip())
        

"""3) Reproduz o seguinte Código que tem como objetivo:
Criar um programa que escreva três linhas num ficheiro novo."""
#resolução ex 3)

with open("novo_ficheiro.txt", "w") as ficheiro:
    ficheiro.write("Linha 1")
    ficheiro.write("Linha 2")
    ficheiro.write("Linha 3")


"""4) Reproduz o seguinte Código que tem como objetivo:
Modificar o programa anterior para acrescentar mais uma linha ao ficheiro."""
#resolução ex 4)

with open("novo_ficheiro.txt", "a") as ficheiro:
    ficheiro.write("Linha adicional")
        

""""5) Reproduz o seguinte código que tem em conta o enunciado a seguir
apresentado :
A empresa DataSecure precisa de um sistema que copie ficheiros binários de forma
eficiente e segura. Para garantir a integridade dos dados, o sistema deve:
a) Solicitar o nome de um ficheiro binário (ex.: imagem, PDF, áudio) que o
utilizador deseja copiar.
b) Criar uma cópia exata desse ficheiro, preservando os dados originais.
c) Verificar se a cópia foi bem-sucedida, comparando os conteúdos dos dois
ficheiros através do cálculo de um hash MD5.
d) Exibir uma mensagem de sucesso ou erro informando se os ficheiros são
idênticos"""   
#resolução ex 5)
 
import hashlib
import os

def calcular_hash(ficheiro):
    """Calcula o hash MD5 de um ficheiro binário para verificar integridade."""
    hash_md5 = hashlib.md5()
    with open(ficheiro, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""): # Lê o ficheiro em blocos de 4KB
            hash_md5.update(chunk)
    return hash_md5.hexdigest()
def copiar_ficheiro_binario(origem, destino):    
    """Copia um ficheiro binário e verifica a integridade dos dados."""
    try:
        # Verificar se o ficheiro de origem existe
        if not os.path.exists(origem):
            print("Erro: O ficheiro de origem não existe.")
            return
        # Copiar o ficheiro binário
        with open(origem, "rb") as f_origem, open(destino, "wb") as f_destino:
            for chunk in iter(lambda: f_origem.read(4096), b""): # Copia em blocos de 4KB
                f_destino.write(chunk)
        # Verificar integridade dos ficheiros
        if calcular_hash(origem) == calcular_hash(destino):
            print(f"Sucesso! O ficheiro '{destino}' foi copiado corretamente.")
        else:
            print("Erro: A cópia do ficheiro não é idêntica ao original.")
    except Exception as e:
        print(f"Erro inesperado: {e}")
        # Solicitar entrada do utilizador
        ficheiro_origem = input("Digite o nome do ficheiro binário a copiar: ")
        ficheiro_destino = "copia_" + ficheiro_origem # Criar nome para o ficheiro copiado
        # Executar a cópia e validação
        copiar_ficheiro_binario(ficheiro_origem, ficheiro_destino)
