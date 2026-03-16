import numpy as np
import matplotlib.pyplot as plt

zbior_x = [10.0**i for i in range(4, 11)]   

def funkcja1(x):
    return(x - np.sqrt(1+x**2))

def funkcja2(x):
    return(-1/(x+np.sqrt(1+x**2)))

y1 = np.array([funkcja1(x) for x in zbior_x])
y2 = np.array([funkcja2(x) for x in zbior_x])
roznica = np.abs(y1-y2)
print(f"({y1}, {y2}), roznica: {roznica}")


plt.figure(figsize=(10, 5))
plt.plot(zbior_x, roznica)
plt.title('Błąd numeryczny')
plt.xlabel('x')
plt.ylabel('błąd')
plt.grid(True, alpha=0.3)
plt.show()