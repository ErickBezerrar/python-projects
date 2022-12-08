limiteInferior = 50
limiteSuperior = 189
numeroDePontos = 1000
h = (limiteSuperior - limiteInferior) / (numeroDePontos - 1)

vX = []
vY = []

i = limiteInferior
while i <= limiteSuperior:
    x = i
    y = x
    vX.append(x)
    vY.append(y)
    i += h

sum = 0
for i in range(len(vX) - 1):
    sum += ((vY[i] + vY[i + 1]) * h) / 2

print("Solução = " + str(sum))
