import numpy as np

J = np.random.randint(1, 11, size=(6, 4))
K = np.random.randint(1, 11, size=(4, 7))

A = np.matmul(J, K)

rref_A = np.linalg.matrix_rank(A)
print("Rank of A:", rref_A)

#A) Construa as matrizes C e N cujas colunas formam bases para Col A e Nul A, respectivamente,
#e construa uma matriz R cujas linhas formam uma base para Row A.
C = A[:, 0:4]
N = np.linalg.null_space(A)
R = A[0:4, :]

print("Matriz C:\n", C)
print("Matriz N:\n", N)
print("Matriz R:\n", R)

#B) Construa uma matriz M cujas colunas formam uma base para Nul A^t, forme as matrizes S = [R^t N] e T = [C M],
#e explique por que S e T devem ser quadradas. Verifique se S e T são invertíveis.
M = np.linalg.null_space(A.T)

S = np.concatenate((R.T, N), axis=1)
T = np.concatenate((C, M), axis=1)

print("Matriz M:\n", M)
print("Matriz S:\n", S)
print("Matriz T:\n", T)

S_inv = np.linalg.inv(S)
T_inv = np.linalg.inv(T)

print("S * inversa(S):\n", np.matmul(S, S_inv))
print("T * inversa(T):\n", np.matmul(T, T_inv))