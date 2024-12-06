import numpy as np

matrix = np.array([[1, 2, 8], [3, 4, 6], [5, 3, 1]])

print(f"Matrix: \n{matrix}")

matrix_list = []
for row in matrix:
    matrix_list.append(row.tolist())

print(f"Matrix's list = {matrix_list}")
print(matrix[1:2, :]) 
print(matrix[2:3, :])  

print(len(matrix)) 
 