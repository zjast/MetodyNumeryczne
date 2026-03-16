import math 
from scipy.integrate import quad

def y(n):
    lista = [math.log(6/5)]
    for i in range(1, n+1):
            lista.append(1/i - 5*lista[-1])
    return lista[n]


def calka(n):
    x_low = 0
    x_high = 1
    funkcja = lambda x: x**n/(x+5)
    return quad(funkcja, x_low, x_high)[0]


n = 24
for i in range(n+1):
    calka_wyn = calka(i)
    rekurencja = y(i)
    print(f"{i}: ", calka_wyn, rekurencja)