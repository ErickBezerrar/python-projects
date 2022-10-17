usuario = int(input("Insira sua velocidade: "))

if usuario <= 80:
    print("Sua velocidade é de 80 km/h, não houve multa")
elif usuario == 90:
    print("Sua velocidade, é de 90 km/h, levou multa leve")
elif usuario >= (91,100):
    print("Sua velocidade é de {usuario} km/h, levou multra grave")
elif usuario > 100:
    print("Sua velocidade é de {usuario} km/h, levou multa gravíssima")
else:
    print("Aí tá certo, rode o programa novamente!")
