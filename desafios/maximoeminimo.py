import matplotlib.pyplot as plt

listFunX = []
listFunY = []

h = 0.000001

def calNumEnt(a, b):

  a = int(a)
  b = int(b)
  
  for i in range(a, b + 1):
    listFunX.append(i)

    funY = f(i)

    listFunY.append(funY)

def f(x):
  y = -x*3 + 12 * x*2 + 60 * x - 4

  return y

def df(x):
  y = (f(x+h) - f(x)) / h

  return y

def df2(x):
  y = (f(x + 2 * h) - 2 * f(x + h) + f(x)) / h**2;

  return y

x = 8
a = x - 10
b = x + 10

def gerarGrafico():
  plt.title("Gráfico da função")  
  plt.xlabel("x")  
  plt.ylabel("y")  
  plt.plot(listFunX, listFunY, color ="blue") 
  plt.show()

calNumEnt(a,b)

gerarGrafico()

for i in range(10):
  x = x - df(x) / df2(x);

print(x)