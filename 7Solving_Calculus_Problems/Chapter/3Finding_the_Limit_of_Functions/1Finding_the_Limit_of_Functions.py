from sympy import Limit, Symbol, S, sin

# Using the function limit and S.Infinity
x = Symbol('x')
print(Limit(1/x, x, S.Infinity))

# Get the limit value
l = Limit(1/x, x, S.Infinity)
print(l.doit())

# Change direction of the limit
l = Limit(1/x, x, 0, dir='-')
print(l.doit())

l = Limit(1/x, x, 0, dir='+')
print(l.doit())

# Limit class handles functions with indeterminate forms
l = Limit(sin(x)/x, x, 0)
print(l.doit())
