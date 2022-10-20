import random
from random import shuffle

print("Esse programa faz uma ordem de apresentação aleatória entre 4 entradas de dados")

p = str(input("Primeiro aluno: "))
s = str(input("Segundo aluno: "))
t = str(input("Terceiro aluno: "))
q = str(input("Quarto aluno: "))

lista = [p,s,t,q]
embaralhar = shuffle((lista))
print(lista)
print("Os valores printados estão em ordem aleatória")