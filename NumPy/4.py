import numpy as np
import Image

A = np.array([[1, 2, 3], [4, 5, 6]])
B = np.array([[7, 8], [9, 10], [11, 12]])

print(f"Матрица A: \n{A}")
print(f"Матрица B: \n{B}")

C = np.dot(A, B)

print(f"Результат перемножения (матрица C): \n{C}")
 