import numpy as np

J = np.random.randint(1, 11, size=(6, 4))
K = np.random.randint(1, 11, size=(4, 7))

A = np.matmul(J, K)

rref_A = np.linalg.matrix_rank(A)
print("Rank of A:", rref_A)

# A) Construct matrices C and N whose columns form bases for Col A and Nul A, respectively,
# and construct a matrix R whose rows form a basis for Row A.

C = A[:, 0:4]
N = np.linalg.null_space(A)
R = A[0:4, :]

print("Matrix C:\n", C)
print("Matrix N:\n", N)
print("Matrix R:\n", R)

# B) Construct a matrix M whose columns form a basis for Nul A^t, form matrices S = [R^t N] and T = [C M],
# and explain why S and T should be square. Check if S and T are invertible.

M = np.linalg.null_space(A.T)

S = np.concatenate((R.T, N), axis=1)
T = np.concatenate((C, M), axis=1)

print("Matrix M:\n", M)
print("Matrix S:\n", S)
print("Matrix T:\n", T)

S_inv = np.linalg.inv(S)
T_inv = np.linalg.inv(T)

print("S * inverse(S):\n", np.matmul(S, S_inv))
print("T * inverse(T):\n", np.matmul(T, T_inv))
