import numpy as np
from scipy.integrate import quad

def metoda_parabol(funkcja, a, b, n):
    if n % 2 != 0:
        n += 1
    h = (b-a)/n
    x = np.linspace(a, b, n+1)
    f =  funkcja(x)
    total = f[0] + f[-1]
    parzyste = np.sum(f[2:n:2])
    nieparzyste = np.sum(f[1:n:2])
    return h/3 * (total + 2*parzyste + 4*nieparzyste)

funkcje = [lambda x: 1+0*x, lambda x: x, lambda x: x**2, lambda x: x**3, lambda x: x**4, lambda x: x**5, lambda x: x**6]
stopnie = [0, 1, 2, 3, 4, 5, 6]

for f, stopien in zip(funkcje, stopnie):
    wynik_dokladny = quad(f, 0, 1)[0]
    wynik = metoda_parabol(f, 0, 1, n=2)
    blad = abs(wynik - wynik_dokladny)
    print(f"Stopień {stopien}: Błąd = {blad:.2e}")
