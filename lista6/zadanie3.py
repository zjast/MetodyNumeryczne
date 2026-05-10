import numpy as np
from scipy.integrate import quad

def romberg(funkcja, a, b, n):
    T = np.zeros((n+1, n+1))
    for i in range(n+1):
        h = (b-a)/(2**i)
        x = np.linspace(a, b, 2**i+1)
        f = funkcja(x)
        T[0, i] = h * (np.sum(f) - 1/2 * (f[0] + f[-1]))

    for m in range(1, n+1):
        for i in range(n + 1 - m):
            T[m, i] = T[m-1, i+1] + (T[m-1, i+1] - T[m-1, i])/(4**m - 1)
    return T

funkcje = [lambda x: 1+0*x, lambda x: x, lambda x: x**2, lambda x: x**3, lambda x: x**4, lambda x: x**5, lambda x: x**6]
stopnie = [0, 1, 2, 3, 4, 5, 6]

for f, stopien in zip(funkcje, stopnie):
    wynik_dokladny = quad(f, 0, 1)[0]
    T = romberg(f, 0, 1, 2)
    wynik = T[2, 0]
    
    blad = abs(wynik - wynik_dokladny)
    print(f"Stopień {stopien}: Błąd = {blad:.2e}")

# Zadanie 4.
funkcja_test = lambda x: np.exp(x)
a, b = 0, 1
n = 6
wynik_dokladny = np.exp(1) - np.exp(0)
T = romberg(funkcja_test, a, b, n)
for i in range(1, n+1):
    wynik = T[i, 0]
    blad = abs(wynik - wynik_dokladny)
    oszacowanie = abs(T[i, 0] - T[i-1, 1])
    roznica = abs(blad - oszacowanie)
    print(f"Błąd: {blad}")
    print(f"Oszacowanie: {oszacowanie}")
    print(f"Różnica między błędem a oszacowaniem: {roznica}")