import math
import numpy as np
import matplotlib

def calculafuncao(funcao, t):
    funcao = funcao.replace("x", str(t))
    resposta = eval(funcao)
    return float (resposta)

def funcaotaxa(funcao,a,b):
    taxa = (calculafuncao(funcao,b) - calculafuncao(funcao,a))/ (b - a)
    return taxa


def funcaoderivada(funcao,x,h):
    Df = (calculafuncao(funcao, x + h) - calculafuncao(funcao, x))/h
    return Df

def testatmv(funcao, lista, a,b,h):
    for i in lista:
        if round(funcaoderivada(funcao,i,h), 2) == funcaotaxa(funcao, a,b):
            print(i)

a = float(input("informe um valor: "))
b = float(input("informe um valor: "))
funcao = input("Digite sua funcão: ")
lista = []
h = 0.0001

for i in np.arange(a,b,0.001):
    lista.append(i)
    
print(testatmv(funcao, lista,a,b,h))