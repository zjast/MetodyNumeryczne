import numpy as np
from scipy.integrate import quad

def poprawiony_romberg(funkcja, a, b, dokladnosc, n):
    T = np.zeros((n+1, n+1))
    for i in range(n+1):
        h = (b-a)/(2**i)
        x = np.linspace(a, b, 2**i+1)
        f = funkcja(x)
        T[0, i] = h * (np.sum(f) - 1/2 * (f[0] + f[-1]))
    for m in range(1, n+1):
        for i in range(n + 1 - m):
            T[m, i] = T[m-1, i+1] + (T[m-1, i+1] - T[m-1, i])/(4**m - 1)
        oszacowanie_bledu = abs(T[m, 0] - T[m-1, 1])
        if oszacowanie_bledu < dokladnosc:
            return T[m, 0], m
    return T[n, 0], n

funkcja = lambda x: np.exp(x)
a, b = 0, 1
dokladnosc = 1e-15
wynik, kroki = poprawiony_romberg(funkcja, a, b, dokladnosc, 20)
wynik_scipy = quad(funkcja, a, b)[0]
roznica = abs(wynik_scipy-wynik)

print(f"Wynik: {wynik} po {kroki} krokach")
print(f"Wynik wbudowanej funkcji: {wynik_scipy}")
print(f"Różnica: {roznica}")
 