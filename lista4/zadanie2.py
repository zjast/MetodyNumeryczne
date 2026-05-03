import numpy as np

n = 500
A = np.random.rand(n,n)
A[-1, :] = np.sum(A[:-1, :], axis=0) + 1e-15
# A = A*1e11

x = np.ones(n)
b = A @ x
calc = np.linalg.solve(A, b)
r = A @ calc - b
norma_r = np.linalg.norm(r)
print(norma_r)

blad = np.linalg.norm(x - calc)
print(blad)

