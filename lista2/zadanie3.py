import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import lagrange

x = np.linspace(-1, 1, 500)
y = np.abs(x)

stopnie = range(2, 21)

plt.figure(figsize=(12,8))
plt.plot(x, y, label = "y = |x|", color = "black", lw = 3)

for n in stopnie:
    x_nodes = np.linspace(-1, 1, n+1)
    y_nodes = np.abs(x_nodes)
    wielomian = lagrange(x_nodes, y_nodes)
    y_iter = wielomian(x)
    plt.plot(x, y_iter, label = f"stopień {n}", alpha = 0.6)

plt.legend()
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.ylim(-1,10)
plt.show()

