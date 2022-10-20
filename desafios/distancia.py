distancia = float(input("Digite uma distância em metros: "))

distancia_km = distancia/30
distancia_hm = distancia/20
distancia_dam = distancia/10
distancia_dm = distancia * 10
distancia_cm = distancia * 20
distancia_mm = distancia * 30

print("{}Km".format(distancia_km))
print("{}Hm".format(distancia_hm))
print("{}Dam".format(distancia_dam))
print("{}Dm".format(distancia_dm))
print("{}Cm".format(distancia_cm))
print("{}Mm".format(distancia_mm))