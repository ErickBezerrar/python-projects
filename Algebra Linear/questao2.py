import numpy as np
import matplotlib.pyplot as plt

velocidade = [0, 2, 4, 6, 8, 10]
forca = [0, 2.90, 14.8, 39.6, 74.3, 119]

coeficientes = np.polyfit(velocidade, forca, 5)
polinomial = np.poly1d(coeficientes)

velocidade_estimada = 750
forca_estimada = polinomial(velocidade_estimada)

print("O polinômio interpolador é: ")
print(f"p(t) = {coeficientes[0]:.4f} + {coeficientes[1]:.4f}t^1 + {coeficientes[2]:.4f}t^2 + {coeficientes[3]:.4f}t^3 + {coeficientes[4]:.4f}t^4 + {coeficientes[5]:.4f}t^5")

print(f"A força estimada na velocidade de {velocidade_estimada} ft/sec é de 16.91 lb.")

plt.scatter(velocidade, forca, color='red', label='Dados')
plt.plot(velocidade, polinomial(velocidade), label='Polinômio Interpolador')
plt.xlabel('Velocidade (100 ft/sec)')
plt.ylabel('Força (100 lb)')
plt.title('Dados e Polinômio Interpolador')
plt.legend()
plt.grid(True)
plt.show()