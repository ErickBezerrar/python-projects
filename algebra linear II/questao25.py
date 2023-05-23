import numpy as np

# Defina a matriz A
A = np.array([[3, 4, 5],
              [7, 4, 3],
              [8, 8, 9]])

# Defina o vetor B
B = np.array([66, 74, 136])

# Combine a matriz A com o vetor B
amp = np.column_stack((A, B))

# Aplique a redução de linha à matriz combinada
rref = np.linalg.matrix_rank(amp) == np.linalg.matrix_rank(A)

# Verifique se o sistema é consistente e encontre a solução
if rref:
    solution = np.linalg.solve(A, B)
    print("O prédio pode ser projetado com o número dado de apartamentos.")
    print("A solução é:")
    print("x1 =", solution[0])
    print("x2 =", solution[1])
    print("x3 =", solution[2])
else:
    print("O prédio não pode ser projetado com o número dado de apartamentos.")
