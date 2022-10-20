km = float(input("Quantos quilômetros você percorreu: "))
dias = int(input("Quantos dias você ficou com o carro: "))

km_carro = km * 0.15
dias_carro = dias * 60

resultado = km_carro + dias_carro
print("O total a pagar é de R${:.2f}".format(resultado))