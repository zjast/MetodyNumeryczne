using Plots

x = range(-10, 1, length=1000)
y = exp.(x)

function szereg(x, n=10)
    return sum((x .^i)/factorial(i) for i in 0:(n-1))
end

function wykres(x,y)
    p = plot(x, y, label="e^x")
    plot!(p, x, szereg(x), label="Szereg Maclaurina", linestyle=:dash)
    plot!(p, ylims=(-1,2))
    display(p)
end

wykres(x, y)

