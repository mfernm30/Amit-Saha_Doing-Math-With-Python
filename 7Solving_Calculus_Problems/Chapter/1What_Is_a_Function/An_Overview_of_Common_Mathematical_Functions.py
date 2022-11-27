import math
import sympy
from sympy import Symbol
from sympy import sin, solve, Symbol

# Using math
print(math.sin(math.pi/2))

# Using sympy
print(sympy.sin(math.pi/2))

theta = Symbol('theta')
# Standard library's sin() function doesnt know what to do when call it with theta, raising and exception
#print(math.sin(theta) + math.sin(theta))
print(sympy.sin(theta) + sympy.sin(theta))

u = Symbol('u')
t = Symbol('t')
g = Symbol('g')
theta = Symbol('theta')
print(solve(u*sin(theta)-g*t, t))
