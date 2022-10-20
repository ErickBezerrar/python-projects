import math
from math import sqrt
# x**x = y**y + z**z

cateto_oposto = float(input("Qual o comprimento do cateto oposto: "))
cateto_adjacente = float(input("Qual o comprimento do cateto adjacente: "))

hipotenusa = cateto_oposto ** 2 + cateto_adjacente ** 2
raiz = sqrt(hipotenusa)

print("A hipotenusa do do triângulo vai medir {:.2f}".format(raiz))