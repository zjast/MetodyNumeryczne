import numpy as np
import matplotlib.pyplot as plt
from numpy.polynomial import Polynomial

x_wykres = np.linspace(0, 10, 500)

# Dla siedmiu punktów kratowych
x = np.array([1, 2, 3, 4, 5, 6, 7])
y = 40 + 10*x + 5*x**2 + 3*x**3 + 2*x**4 + x**5 + x**6

wielomian = Polynomial.fit(x, y, 6)
y_wykres = wielomian(x_wykres)

plt.figure(figsize=(10, 6))
plt.plot(x_wykres, y_wykres, label="Wielomian")
plt.scatter(x, y, color="red", label="punkty kratowe")

plt.title("Aproksymacja wielomianem")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True, linestyle="--", alpha=0.7)
plt.tight_layout()
plt.show()

# Dla większej ilości punktów
x2 = np.linspace(1, 10, 50)
y2 = 40 + 10*x2 + 5*x2**2 + 3*x2**3 + 2*x2**4 + x2**5 + x2**6
wielomian2 = Polynomial.fit(x2, y2, 6)
y_wykres2 = wielomian2(x2)

plt.figure(figsize=(10, 6))
plt.plot(x2, y_wykres2, label="Wielomian")
plt.scatter(x2, y2, color="red", label="punkty kratowe")
plt.title("Aproksymacja wielomianem dla większej ilości punktów")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True, linestyle="--", alpha=0.7)
plt.tight_layout()
plt.show()