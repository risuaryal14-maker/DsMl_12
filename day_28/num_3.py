print('first=========>')
import numpy as np
#result_max=matrix_1 * matrix_2 wrong concept
#result_max
print('matriz_1',[[1, 2, 3], [4, 5, 6]])
print('matriz_2',[[7, 8, 9],
                 [10,11,12]])
matrix_1 = np.array([[1, 2, 3], 
                     [4, 5, 6]])
matrix_2 = np.array([[7, 8, 9],
                    [10,11,12]])
#result_max = np.dot(matrix_1, matrix_2.T)  # Use dot product
result_max=matrix_1 * matrix_2

print(result_max)

print('second=========>')
#element wise operation with scalars
print(matrix_1) 
print('////////////////')

scalar=2
result_add = matrix_1 + scalar
print('result_add:',result_add)

print('third=========>')
a=np.array([[2,1],
           [1,3]])
b=np.array([5,6])
x=np.linalg.solve(a,b)
print('solution:',x)

print('fourth=========>')
#find the slope and intercept of a line using the normal equation
x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 6, 8, 10])
X = np.column_stack((np.ones_like(x), x))
w = np.linalg.inv(X.T @ X) @ X.T @ y
print('slope:',w[0])
print('intercept:',w[1])
