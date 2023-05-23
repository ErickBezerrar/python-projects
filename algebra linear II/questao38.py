import numpy as np

np.random.seed(0)  # Definindo uma semente para reprodutibilidade

for i in range(3, 6):
    J = np.random.randint(1, 11, size=(5, i))
    K = np.random.randint(1, 11, size=(i, 7))

    A = np.matmul(J, K)
    rref_A = np.linalg.matrix_rank(A)

    print("A:\n", A)
    print("Posto de A:", rref_A)

    posto_A = np.linalg.matrix_rank(A)
    C = A[:, 0:i]
    R = posto_A[0:i, :]

    CR = np.matmul(C, R)
    print("CR:\n", CR)
    print("-------------------")
