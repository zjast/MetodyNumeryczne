import numpy as np

zbior_x = [10.0**i for i in range(4, 11)]   

def funkcja1(x):
    return(x - np.sqrt(1+x**2))

def funkcja2(x):
    return(-1/(x+np.sqrt(1+x**2)))

for i in zbior_x:
    roznica = abs(funkcja1(i)-funkcja2(i))
    print(f"({funkcja1(i)}, {funkcja2(i)}), roznica: {roznica}")