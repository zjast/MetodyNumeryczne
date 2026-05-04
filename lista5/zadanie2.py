import numpy as np

def jacobi(A, b, p):
    n = len(b)
    x = [0] * n
    x_nowe = [0] * n
    for i in range(p):
        for j in range(n):
            suma = 0
            for k in range(n):
                if j != k:
                    suma += A[j][k] * x[k]
            x_nowe[j] = (b[j] - suma) / A[j][j]
        for l in range(n):
            x[l] = x_nowe[l]
    return x

if __name__ == "__main__":
    A = np.array([[ 3,  1, -1],
                  [-3,  8,  2],
                  [-2,  1,  4]])

    b = np.array([2, 19, 12])
    sprawdzenie = np.linalg.solve(A, b)
    print(sprawdzenie)
    wyniki = jacobi(A, b, 16)
    print(wyniki)

    norma = np.linalg.norm(A @ wyniki - b)
    print(norma)

