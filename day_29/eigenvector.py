import numpy as np
A = np.array([[4, 2], [1, 3]])
eigenvalues, eigenvectors = np.linalg.eig(A)
print("Eigenvalues:", eigenvalues)
print('*\n'*3)

  
print("Eigenvectors:", eigenvectors)


print('second=========>')
import numpy as np
A = np.array([[4, 2], [1, 3]])
#performing SVD
U, S, V = np.linalg.svd(A)
print("U matrix:\n",U)
print('sigma values:',S)
print('V matrix:\n',V)
print('unitary matrix:\n',U @ U.T)