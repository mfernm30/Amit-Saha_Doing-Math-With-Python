from sympy import Symbol
from sympy import solve

x = Symbol('x')
y = Symbol('y')

expr1 = 2*x + 3*y - 6
expr2 = 3*x + 2*y - 12

print(solve((expr1, expr2), dict=True))

#We can check if the result is correct.
soln = solve((expr1, expr2), dict=True)
soln = soln[0]
print(expr1.subs({x:soln[x], y:soln[y]}))
print(expr2.subs({x:soln[x], y:soln[y]}))
