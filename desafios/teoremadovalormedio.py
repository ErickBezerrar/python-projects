import math
import 

a = int(input("informe um valor: "))
b = int(input("informe um valor: "))
f = 0
h = 0.0001


def testatmv(f,a,b):
    for x in range(a,b,0.0001):
        print(x)


testatmv(f,a,b)