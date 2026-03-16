import numpy as np

przedzial = np.linspace(1 - 1e-3, 1 + 1e-3, 100)

def funkcja1(x):
    return((x-1)**4)

def funkcja2(x):
    return(x**4 - 4*x**3 + 6*x**2 - 4*x +1)

for x in przedzial:
    roznica = abs(funkcja1(x) - funkcja2(x))
    print(f"({funkcja1(x)}, {funkcja2(x)}, roznica: {roznica})")


