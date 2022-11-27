from sympy import Symbol
'''
Produces and exception, Sympy doesnt know the sign of x
x = Symbol('x')
if (x+5) > 0:
    print('Do Something')
else:
    print('Do Something else')
'''

# Assumptions: declare symbol as positive, negative, real, integer, complex, imaginary
x = Symbol('x', positive=True)
if (x+5) > 0:
    print('Do Something')
else:
    print('Do Something else')
