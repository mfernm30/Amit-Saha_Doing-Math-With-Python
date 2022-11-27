from sympy import Derivative, Symbol
from sympy import Symbol, Derivative

t = Symbol('t')
St = 5*t**2 + 2*t + 8

d = Derivative(St, t)
print(d)
print(d.doit())

x = Symbol('x')
f = (x**3 + x**2 + x)*(x**2+x)

print(Derivative(f, x).doit())
