import numpy as np

A = np.array([[1, 1, 2, 1], 
              [0, 1, 4, 3],
              [4, 6, 8, 6],
              [5, 5, -5, 5]])

B = np.array([[2, 1, 2, 1], 
              [1, 2, 1, 2], 
              [2, 1, 2, 1],
              [2, 2, 2, 2]])

det_A = np.linalg.det(A)
det_B = np.linalg.det(B)
print(det_A)
print(det_B)