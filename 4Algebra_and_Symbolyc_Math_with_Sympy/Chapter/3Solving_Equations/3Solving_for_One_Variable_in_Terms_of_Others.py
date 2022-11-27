from sympy import Symbol, solve, pprint

x = Symbol('x')
a = Symbol('a')
b = Symbol('b')
c = Symbol('c')

expr = a*x*x + b*x + c
print(solve(expr, x, dict=True))

#This example is more clear. Uses one of the equations of motion. Solve the equation in terms of the time variable.
from sympy import Symbol, solve, pprint

s = Symbol('s')
u = Symbol('u')
t = Symbol('t')
a = Symbol('a')

expr = u*t + (1/2)*a*t*t - s
t_expr = solve(expr,t, dict=True) 

pprint(t_expr)