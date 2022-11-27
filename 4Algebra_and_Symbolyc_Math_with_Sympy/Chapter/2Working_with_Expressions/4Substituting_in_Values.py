from sympy import Symbol
from sympy import simplify

x = Symbol('x')
y = Symbol('y')
expr = x*x + x*y + x*y + y*y
#Using subs method to substitute the expresion with a certain value.
res = expr.subs({x:1, y:2})
print(res)
#Using subs method to substitute the expresion with another expression
res = expr.subs({x:1-y})
print(res)
#Simplify the expression (Sympy won't do any simplification wihout being asked to)
expr_subs = expr.subs({x:1-y})
print(simplify(expr_subs))