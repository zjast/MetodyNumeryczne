import numpy as np

n = 250
A = np.random.rand(n,n)
A[-1, :] = np.sum(A[:-1, :], axis=0) + 1e-15
x = np.ones(n)
b = np.dot(A, x)
sol = np.linalg.solve(A, b)
r = np.dot(A, sol) - b

print(f"{np.linalg.norm(r):.2e}")