from sympy import Symbol
from sympy import symbols

x  = Symbol('x')
print(x + x + 1)

# Label not necesarry must be the same name as symbol, but its recommend if you use the same symbol and label
a = Symbol('x')
print(a + a + 1)

# Create various symbols
x = Symbol('x')
x = Symbol('y')
x = Symbol('z')
x, y, z = symbols('x, y, z')

# You can use operators between symbols (+, -, /, *, and **)
s = x*y + x*y
p = x*(x + x)
t = (x + 2)*(x + 3)
print(s)
print(p)
print(t)

