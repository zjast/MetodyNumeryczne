import numpy as np
import matplotlib.pyplot as plt

przedzial = np.linspace(1 - 1e-3, 1 + 1e-3, 100)

def funkcja1(x):
    return((x-1)**4)

def funkcja2(x):
    return(x**4 - 4*x**3 + 6*x**2 - 4*x +1)

y1 = funkcja1(przedzial)
y2 = funkcja2(przedzial)
roznica = np.abs(y1 - y2)


plt.figure(figsize=(10, 5))
plt.plot(przedzial, roznica, color='red', linewidth=0.8)
plt.title('Błąd numeryczny')
plt.xlabel('x')
plt.ylabel('roznica')
plt.grid(True, alpha=0.3)
plt.show()
