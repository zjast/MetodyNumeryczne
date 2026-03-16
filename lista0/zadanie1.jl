using QuadGK

function y(n)
    lista = BigFloat[log(BigFloat(6)/5)]
    for i in 1:n
        append!(lista, 1/BigFloat(i) - 5*lista[end])
    end
    return lista[n+1]
end

function calka(n)
    x_low = 0
    x_high = 1
    funkcja = x -> x^n/(x+5)
    return quadgk(funkcja, x_low, x_high)[1]
end

n = 24
for i in 0:n
    calka_wyn = calka(i)
    rekurencja = y(i)
    println(calka_wyn, " ", rekurencja)
end


