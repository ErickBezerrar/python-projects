import numpy as np

# Define the matrix A
A = np.array([[3, 4, 5],
              [7, 4, 3],
              [8, 8, 9]])

# Define the vector B
B = np.array([66, 74, 136])

# Augment matrix A with vector B
amp = np.column_stack((A, B))

# Apply row reduction to the augmented matrix
rref = np.linalg.matrix_rank(amp) == np.linalg.matrix_rank(A)

# Check if the system is consistent and find the solution
if rref:
    solution = np.linalg.solve(A, B)
    print("The building can be designed with the given number of apartments.")
    print("The solution is:")
    print("x1 =", solution[0])
    print("x2 =", solution[1])
    print("x3 =", solution[2])
else:
    print("The building cannot be designed with the given number of apartments.")
