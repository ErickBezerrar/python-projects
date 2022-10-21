from random import choice
from random import shuffle

p = str(input("Primeiro aluno: "))
s = str(input("Segundo aluno: "))
t = str(input("Terceiro aluno: "))
q = str(input("Quarto aluno: "))

lista = [p,s,t,q]
embaralhar = shuffle(lista)
escolha = choice(lista)
print(escolha)