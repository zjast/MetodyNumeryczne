import numpy as np
from scipy.linalg import hilbert

najlepsze_n = 0
najwieksze_r = 0

for n in range(1,10):
    try: 
        A = hilbert(n)
        x = np.ones(n)
        b = np.dot(A, x)
        x_wynik = np.linalg.solve(A, b)
        r = np.dot(A, x_wynik) - b
        blad = np.linalg.norm(r)

        if blad > najwieksze_r:
            najwieksze_r = blad
            najlepsze_n = n

    except np.linalg.LinAlgError:
        continue

print(f"największe r: {najwieksze_r} dla macierzy rozmiaru: {najlepsze_n}")