def wynik_eps(a):
    epsilon = 1
    n = 0
    while a+ epsilon/2 > a:
        epsilon = epsilon/2
        n = n+1
    return n, epsilon

print(wynik_eps(1))    # część pierwsza a = 1

wartosci = [10, 100, 1000,10000]
for a in wartosci:
    n, eps = wynik_eps(a)
    print(f"a = {a}, n = {n}, epsilon = {eps} ")

