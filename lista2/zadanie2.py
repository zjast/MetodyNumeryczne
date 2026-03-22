import heapq

ciag = lambda i: (1/3)**i
# Sposób 1.
def pierwszy(n):
    return sum(ciag(i) for i in range(1, n+1))

# Sposób 2.
def drugi(n):
    suma = 0
    for i in range(1, n+1):
        wynik = ciag(i)
        suma = suma + wynik
    return suma

# Sposób 3.
def trzeci(n):
    suma = 0
    for i in range(n, 0, -1):
        wynik = ciag(i)
        suma = suma + wynik
    return suma

# Sposób 4.
def czwarty(n):
    lista = [ciag(i) for i in range(1, n+1)]
    heapq.heapify(lista)
    while len(lista)>1:
        pierwszy = heapq.heappop(lista)
        drugi = heapq.heappop(lista)
        suma = pierwszy + drugi
        heapq.heappush(lista, suma)
    return lista[0]


n = 10*10
wynik1 = pierwszy(n)
wynik2 = drugi(n)
wynik3 = trzeci(n)
wynik4 = czwarty(n)
print(f"Sposób 1: {wynik1}, \nSposób 2: {wynik2}, \nSposób 3: {wynik3}, \nSposób 4: {wynik4}")
