altura = float(input("Insira a altura da parede em metros: "))
largura = float(input("Insira a largura da parede em metros: "))

total_parede = altura * largura
print("Sua parede tem dimensão de {}x{} e sua área é de {}m2".format(altura, largura, total_parede))
tinta = total_parede / 2
print("Para pintar essa parede você precisará de {} litros".format(tinta))