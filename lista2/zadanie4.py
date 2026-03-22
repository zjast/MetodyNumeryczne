import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import lagrange

x = np.linspace(-1, 1, 21)
y = 1/(1+25*x**2)

wielomian = lagrange(x,y)

x_wykres = np.linspace(-1,1, 500)
y_wykres = 1/(1+25*x_wykres**2)
y_inter = wielomian(x_wykres)

plt.plot(x_wykres, y_wykres, label = "y=1/(1+25x^2)")
plt.plot(x_wykres, y_inter, label = "interpolacja")
plt.legend()
plt.grid(True)
plt.show()