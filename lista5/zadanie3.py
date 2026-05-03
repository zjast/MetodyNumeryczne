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
                         [5, 5, -5, 16]], dtype=float)

b = [22, 40, 100, 64]

wynik_wbudowany = np.linalg.solve(A_dominujaca, b)
norma_wbudowany = np.linalg.norm(A_dominujaca @ wynik_wbudowany - b)
print(f"Wynik metody wbudowanej dla macierzy A: {wynik_wbudowany}, norma: {norma_wbudowany}")

wynik_gauss = gauss(A_dominujaca.copy(), b.copy())
norma_gauss = np.linalg.norm(A_dominujaca @ wynik_gauss - b)
print(f"Wynik Gauss dla macierzy A: {wynik_gauss}, norma: {norma_gauss}")

n = len(b)
iteracje = [n, n**2, n**3]
wynik_wbudowany2 = np.linalg.solve(A_dominujaca, b)
print(f"Wynik dla metody Jacobiego: {wynik_wbudowany2}")

for i in iteracje:
    wynik_jacobi = jacobi(A_dominujaca.copy(), b.copy(), i)
    norma_jacobi = np.linalg.norm(A_dominujaca @ wynik_jacobi - b)
    print(f"Wynik Jacobi dla macierzy A po {i} iteracjach: {wynik_jacobi}, norma: {norma_jacobi}")