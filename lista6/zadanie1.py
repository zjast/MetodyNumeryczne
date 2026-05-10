import numpy as np
from scipy.integrate import quad

def metoda_trapez(funkcja, a, b, n):
    wysokosc = (b-a)/n
    total = 0
    for i in range(n):
        x = a + wysokosc*i
        total += wysokosc * (funkcja(x) + funkcja(x+wysokosc))/2
    return total

funkcje = [lambda x: 1+0*x, lambda x: x, lambda x: x**2, lambda x: x**3, lambda x: x**4, lambda x: x**5, lambda x: x**6]
stopnie = [0, 1, 2, 3, 4, 5, 6]

for f, stopien in zip(funkcje, stopnie):
    wynik_dokladny = quad(f, 0, 1)[0]
    wynik = metoda_trapez(f, 0, 1, n=2)
    blad = abs(wynik - wynik_dokladny)
    print(f"Stopień {stopien}: Błąd = {blad:.2e}")
