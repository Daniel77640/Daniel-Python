"""Considera a seguinte lista:
nums=[10, 2.5, 7, 11, 7.9, "Python", True,6, 5.8 , "Listas"]
Efetua um programa em python que:
a. Imprima a quantidade de numeros inteiros, floats, strings e boleanos na lista;
b. Efetua a média de todos os valores inteiros na lista.
c. Crie e retorne uma nova lista só com os valores inteiros"""

nums=[10, 2.5, 7, 11, 7.9, "Python", True,6, 5.8 , "Listas"]
nums1=[10, 7, 11, 6]
nums2=[2.5, 7.9, 5.8]
nums3=["Phyton", "listas"]
nums4=[True]

from statistics import mean
print(f"inteiros {nums1}")
print(f"floats {nums2}")
print(f"strings {nums3}")
print(f"boleanos {nums4}")
print (f"media {mean(nums2)}")
print (nums1)


#resolução
"""isinstance(x,int) and not isinstance(x,bool)
isinstance(x,float)
isinstance(x,str)

type(x)==int
type(x)==bool
type(x)==str
type(x)==float"""

nums=[10, 2.5, 7, 11, 7.9, "Python", True,6, 5.8 , "Listas"]
type(nums)==int
type(nums)==float
type(nums)==str
type(nums)==bool
print (mean (type(nums)==int))