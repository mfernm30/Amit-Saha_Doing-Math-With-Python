from sympy import solve
from sympy import Symbol

x = Symbol('x')
expr = x**2 + 5*x + 4

print(solve(expr, dict=True))

#Printing the roots of this equation that i know that will give me a complex result.
x=Symbol('x')
expr = x**2 + x + 1
print(solve(expr, dict=True))