import numpy as np
import matplotlib.pyplot as plt
from numpy.polynomial import Polynomial

x = np.linspace(-1, 1, 500)
y = 1/(1+25*x**2)

stopnie = range(1, 21)
colors = plt.cm.Spectral(np.linspace(0,1,len(stopnie)))

plt.figure(figsize=(12,8))
plt.plot(x, y, label = "y = 1 / (1+25*x^2)", color = "black", lw = 2)

for n, kolor in zip(stopnie, colors):
    p = Polynomial.fit(x, y, n)
    y_app = p(x)
    plt.plot(x, y_app, label = f"Wielomian stopnia {n}", color = kolor, lw = 1, alpha = 0.7)

plt.legend()
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.ylim(-0.5, 1.5)
plt.show()