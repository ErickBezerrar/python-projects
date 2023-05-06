import numpy as np
import matplotlib.pyplot as plt

velocity = [0, 2, 4, 6, 8, 10]
force = [0, 2.90, 14.8, 39.6, 74.3, 119]

coefficients = np.polyfit(velocity, force, 5)
polynomial = np.poly1d(coefficients)

velocity_estimate = 750
force_estimate = polynomial(velocity_estimate)

plt.scatter(velocity, force, color='red', label='Dados')
plt.plot(velocity, polynomial(velocity), label='Polinômio Interpolador')
plt.xlabel('Velocidade (100 ft/sec)')
plt.ylabel('Força (100 lb)')
plt.title('Dados e Polinômio Interpolador')
plt.legend()
plt.show()

print("O polinômio interpolador é: ")
print(f"p(t) = {coefficients[5]:.4f} + {coefficients[4]:.4f}t + {coefficients[3]:.4f}t^2 + {coefficients[2]:.4f}t^3 + {coefficients[1]:.4f}t^4 + {coefficients[0]:.4f}t^5")

print(f"A força estimada na velocidade de {velocity_estimate} ft/sec é de {force_estimate:.4f} lb.")
