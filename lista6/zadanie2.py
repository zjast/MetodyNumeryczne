import numpy as np

def parabola(funkcja, a, b, n):
    przedzial = (b-a)/n
    total = 0
    for i in range(0, n, 2):
        x = a + przedzial * 2 * i
        total += przedzial * funkcja(x) + 4* funkcja(x + przedzial) + funkcja(x+2*przedzial) / 3
    return total

funkcja = lambda x: x**2
wynik = parabola(funkcja, 0, 1, 100)
print(wynik)
