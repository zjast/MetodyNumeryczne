import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline

x = np.linspace(-1, 1, 500)
y = np.abs(x)

punkty_kratowe = range(4, 21)
colors = plt.cm.Spectral(np.linspace(0,1,len(punkty_kratowe)))

plt.figure(figsize=(12,8))
plt.plot(x, y, label = "y = |x|", color = "black", lw = 2)

for n, kolor in zip(punkty_kratowe, colors):
    x_kratowe = np.linspace(-1, 1, n)
    y_kratowe = np.abs(x_kratowe)
    f_sklejana = make_interp_spline(x_kratowe, y_kratowe, k = 3)
    y_wart = f_sklejana(x)
    plt.plot(x, y_wart, label = f"Wielomian sklejany dla {n} wezłów", color = kolor, lw = 1, alpha = 0.7)

plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.ylim(-0.1, 1.25)
plt.show()