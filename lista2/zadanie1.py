import heapq

# Sposób 1.
def pierwszy(n):
    return sum(1/i**2 for i in range(1, n+1))

# Sposób 2.
def drugi(n):
    suma = 0
    for i in range(1, n+1):
        wynik = 1/i**2
        suma = suma + wynik
    return suma

# Sposób 3.
def trzeci(n):
    suma = 0
    for i in range(n, 0, -1):
        wynik = 1/i**2
        suma = suma + wynik
    return suma

# Sposób 4.
def czwarty(n):
    lista = [1/i**2 for i in range(1, n+1)]
    kopiec = lista
    heapq.heapify(kopiec)
    while len(kopiec)>1:
        pierwszy = heapq.heappop(kopiec)
        drugi = heapq.heappop(kopiec)
        suma = pierwszy + drugi
        heapq.heappush(kopiec, suma)
    return kopiec[0]

n = 10**6
wynik1 = pierwszy(n)
wynik2 = drugi(n)
wynik3 = trzeci(n)
wynik4 = czwarty(n)
print(f"Sposób 1: {wynik1}, \nSposób 2: {wynik2}, \nSposób 3: {wynik3}, \nSposób 4: {wynik4}")
