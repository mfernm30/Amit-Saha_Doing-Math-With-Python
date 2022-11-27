from sympy import Symbol, exp, sqrt, pi, Integral, S

x = Symbol('x')
p = exp(-(x - 10)**2/2)/sqrt(2*pi)

print(Integral(p, (x, 11, 12)).doit().evalf())
print(Integral(p, (x, S.NegativeInfinity, S.Infinity)).doit().evalf())