import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import lagrange

x = np.linspace(-1, 1, 500)

def funkcja(x):
    return 1/(1 + 25*x**2)
y = funkcja(x)

stopnie = range(2, 21, 2)

plt.figure(figsize=(12,8))
plt.plot(x, y, label = "y=1/(1+25x^2)", color = "black", lw = 3)

for n in stopnie:
    x_nodes = np.linspace(-1, 1, n+1)
    y_nodes = funkcja(x_nodes)
    wielomian = lagrange(x_nodes, y_nodes)
    y_iter = wielomian(x)
    plt.plot(x, y_iter, label = f"stopień {n}", alpha = 0.6)

plt.legend()
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.ylim(-1,5)
plt.show()
