from random import shuffle


idades = [15,46,75,34,23]
print(sum(idades))
print(idades[0] + idades[1] + idades[2] + idades[3] + idades[4])
shuffle(idades)
print(idades)

nomes = ["Jhonatan", "Caio", "Pedro", "Colchetes", "Direta"]
shuffle(nomes)
print(nomes)