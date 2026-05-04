import numpy as np

def gauss(A, b):
    n = len(b)
    for i in range(n):
        if A[i][i] == 0:
            raise ValueError
        for j in range(i+1, n):
            p = A[j][i] / A[i][i]
            for k in range(i, n):
                A[j][k] -= p * A[i][k]
            b[j] = b[j] - p * b[i]
    x = [0] * n
    for i in range(n - 1, -1, -1):
        suma = 0
        for j in range(i + 1, n):
            suma = suma + (A[i][j] * x[j])
        x[i] = (b[i] - suma) / A[i][i]
    return x

if __name__ == "__main__":
    A = np.array([[ 3,  1, -1],
                  [-3,  8,  2],
                  [-2,  1,  4]])

    b = np.array([2, 19, 12])
    wyniki = gauss(A, b)
    sprawdzenie = np.linalg.solve(A, b)
    print(sprawdzenie)
    print(wyniki)

    norma = np.linalg.norm(A @ wyniki - b)
    print(norma)




