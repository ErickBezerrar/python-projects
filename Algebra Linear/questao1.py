import numpy as np
import matplotlib.pyplot as plt

x = np.array([1, 2, 3])
y = np.array([6, 15, 28])
A = np.array([[1, 1, 1],[1, 2, 4],[1, 3, 9]])
b = np.array([6, 15, 28])

x_interpolacao = np.linalg.solve(A, b)

a0, a1, a2 = x_interpolacao

t = np.linspace(1, 3, 100)

(p) = a0 + a1*t + a2*t**2

plt.scatter(x, y, label='Pontos', color='red')
plt.plot(t, p, label='Polinômio interpolador')
plt.title('Interpolação polinomial')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()