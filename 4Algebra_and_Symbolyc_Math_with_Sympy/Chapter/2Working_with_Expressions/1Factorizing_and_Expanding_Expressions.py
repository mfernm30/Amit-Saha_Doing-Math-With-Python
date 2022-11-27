from sympy import Symbol
from sympy import factor
from sympy import expand

#Expression1 factorized and then expanded then print the result.
x = Symbol('x')
y = Symbol('y')
expr1 = x**2 - y**2
factors = factor(expr1)
expanded = expand(factors)
print(expr1)
print(factors)
print(expanded)

#Expression2 factorized and then expanded then print the result.
expr2 = x**3 + 3*x**2*y + 3*x*y**2 + y**3
factors = factor(expr2)
expanded = expand(factors)
print(expr2)
print(factors)
print(expanded)



