import numpy as np 

def trapez(funkcja, a, b, n):
    wysokosc = (b-a)/n
    total = 0
    for i in range(n):
        x = a + wysokosc*i
        total += wysokosc * (funkcja(x) + funkcja(x+wysokosc))/2
    return total

funkcja = lambda x: x**2
wynik = trapez(funkcja, 0, 1, 100)
print(wynik)
