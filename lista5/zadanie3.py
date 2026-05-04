import numpy as np
from zadanie1 import gauss
from zadanie2 import jacobi

A = np.array([[1, 1, 2, 1], 
              [0, 1, 4, 3],
              [4, 6, 8, 6],
              [5, 5, -5, 5]])

B = np.array([[2, 1, 1, 2], 
              [1, 2, 1, 2], 
              [2, 1, 2, 1],
              [2, 2, 2, 2]])

A_dominujaca = np.array([[10, 1, 2, 1], 
                         [0, 8, 4, 3],
                         [4, 6, 20, 6],
                         [5, 5, -5, 16]])

b1 = np.array([1, 0, 4, 5])
b2 = np.array([22, 40, 100, 64])

wynik_wbudowany = np.linalg.solve(A, b1)
norma_wbudowany = np.linalg.norm(A @ wynik_wbudowany - b1)
print(f"Wynik metody wbudowanej dla macierzy A: {wynik_wbudowany}, norma: {norma_wbudowany}")

wynik_gauss = gauss(A.copy(), b1.copy())
norma_gauss = np.linalg.norm(A @ wynik_gauss - b1)
print(f"Wynik Gauss dla macierzy A: {wynik_gauss}, norma: {norma_gauss}")

n = len(b2)
iteracje = [n, n**2, n**3]
wynik_wbudowany2 = np.linalg.solve(A, b2)
print(f"Wynik dla metody Jacobiego: {wynik_wbudowany2}")

for i in iteracje:
    wynik_jacobi = jacobi(A.copy(), b2.copy(), i)
    norma_jacobi = np.linalg.norm(A @ wynik_jacobi - b2)
    print(f"Wynik Jacobi dla macierzy A po {i} iteracjach: {wynik_jacobi}, norma: {norma_jacobi}")