import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import lagrange

x = np.linspace(-1, 1, 21)
y = np.abs(x)

wielomian = lagrange(x,y)

x_wykres = np.linspace(-1,1, 500)
y_wykres = np.abs(x_wykres)
y_inter = wielomian(x_wykres)

plt.plot(x_wykres, y_wykres, label = "y=|x|")
plt.plot(x_wykres, y_inter, label = "interpolacja")
plt.legend()
plt.grid(True)
plt.show()

