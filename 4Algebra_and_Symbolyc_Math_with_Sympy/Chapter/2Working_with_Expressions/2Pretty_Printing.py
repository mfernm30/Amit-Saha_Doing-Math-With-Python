from sympy import pprint
from sympy import Symbol
from sympy import init_printing

# Using pprint to print the expression resembling how we'd normally write it on paper
x = Symbol('x')
y = Symbol('y')

expr = x*x + 2*x*y + y*y
pprint(expr)

# Changing the order to visualize the expression
init_printing(order='rev-lex')
pprint(expr)
