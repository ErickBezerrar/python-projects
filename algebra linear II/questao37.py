import numpy as np

A = np.array([[7, -9, -4, 5, 3, -3, -7],
[-4, 6, 7, -2, -6, -5, 5],
[5, -7, -6, 5, -6, 2, 8],
[-3, 5, 8, -1, -7, -4, 8],
[6, -8, -5, 4, 4, 9, 3]])

rref_A = np.linalg.matrix_rank(A)
print("Posto de A:", rref_A)

esc = np.linalg.matrix_rank(A)
C = np.concatenate((A[:, [0, 1]], A[:, [3]], A[:, [5]]), axis=1)
R = esc[0:4, :]

print("Matriz C:\n", C)
print("Matriz R:\n", R)

CR = np.matmul(C, R)
print("CR:\n", CR)