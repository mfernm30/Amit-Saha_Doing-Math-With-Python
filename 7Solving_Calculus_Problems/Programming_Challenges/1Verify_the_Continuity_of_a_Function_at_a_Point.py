'''
Verify the Continuity of a Function at a Point
'''
from sympy import Symbol, Derivative, Limit, sympify, pprint
from sympy.core.sympify import SympifyError


def continous(f, var, p):
    d = Derivative(f, var).doit()
    l_left = Limit(f, var, p, dir='-')
    l_right = Limit(f, var, p, dir='+')
    f_p = f.subs({var: p})
    if (l_left.doit() == l_right.doit() == f_p):
        print("{0} is continuous at {1}".format(f, p))
    else:
        print("{0} is not continuous at {1}".format(f, p))


if __name__ == '__main__':
    f = input('Enter a function in one variable: ')
    var = input('Enter the variable: ')
    p = input('Enter the point to check the continuty at: ')
    try:
        f = sympify(f)
    except SympifyError:
        print('Invalid input')
    else:
        continous(f, var, p)
