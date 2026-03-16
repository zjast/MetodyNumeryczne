def x(i):
    lista = [1, 1/5]
    for _ in range(i-1):
        lista.append((26*lista[-1] - 5*lista[-2])/5)
    return lista

def wstecz(x_koniec, x_przedostatni, N):
    lista = [x_koniec, x_przedostatni]
    for _ in range(N-1):
        lista.append((26*lista[-1] - 5*lista[-2])/5)
    return lista

N = 30
wyniki = x(N)
x_koniec = wyniki[-1]
x_przedostatni = wyniki[-2]

lista_tyl = wstecz(x_koniec, x_przedostatni, N)[::-1]
print((wyniki[29], wyniki[30]))
print((lista_tyl[0], lista_tyl[1]), (wyniki[0], wyniki[1]))

def y(i):
    lista = [1, 1/2]
    for _ in range(i):
        lista.append((5*lista[-1]-2*lista[-2])/2)
    return lista[i]

print(y(30))