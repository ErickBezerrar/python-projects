import turtle
tartaruga = turtle.Turtle()
tartaruga.shape("turtle")
tartaruga.color("medium aquamarine")

for palavra in range(1,4):
    print("Carregando...")

x = 5

for lista in range(1,20):
    print(lista)
    
print("===========")
for lista_dois in range(1,20,2):
    print(lista_dois)
    
print("===========")
for lista_tres in range(1,101,x):
    print(lista_tres)

