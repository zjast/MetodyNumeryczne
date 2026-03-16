import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-10, 1, 0.001)
y = np.exp(x)


def szereg(x, n = 10):
    lista = [1]
    for i in range(1,n):
        lista.append(lista[-1]*x/i)
    return sum(lista)

def wykres(x, y):
    plt.plot(x, y, label="Exp")
    plt.plot(x, szereg(x), label="Szereg Maclaurina", linestyle="dashed")
    plt.legend()
    plt.ylim(-1, 2)
    plt.show()

wykres(x,y)