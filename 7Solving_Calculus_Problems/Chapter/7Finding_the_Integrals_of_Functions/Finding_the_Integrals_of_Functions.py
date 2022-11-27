from sympy import Integral, Symbol

x = Symbol('x')
k = Symbol('k')
print(Integral(k*x, x).doit())

# Definitive itegral
print(Integral(k*x, (x, 0, 2)).doit())

# Definitive integral between 2 and 4 in x function
x = Symbol('x')
print(Integral(x, (x, 2, 4)).doit())
