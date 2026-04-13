import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import approximate_taylor_polynomial

x = np.linspace(-1, 1, 500)
def funkcja(x):
    return np.abs(x)

y = funkcja(x)

stopnie = range(1,21)
plt.figure(figsize=(12,8))
plt.plot(x, y, label = "y = |x|", color = "black", lw = 3)

for n in stopnie:
    x_nodes = np.linspace(-1, 1, n+1)
    y_nodes = np.abs(x_nodes)
    wielomian = np.polyfit(x_nodes, y_nodes, 1)
    y_iter = np.poly1d(wielomian)
    plt.plot(x, y_iter, label = f"stopień {n}", alpha = 0.6)

plt.legend()
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.ylim(-1,10)
plt.show()



