'''
Derivative calculator

You can calculate partial derivatives with this example:
Enter a function: 2*x*y + x*y**2
Enter the variable to differentiate with respect to: x
Result: y 2 + 2·y
'''
from sympy import Symbol, Derivative, sympify, pprint
from sympy.core.sympify import SympifyError


def derivative(f, var):
    var = Symbol(var)
    d = Derivative(f, var).doit()
    pprint(d)


if __name__ == '__main__':
    f = input('Enter a function: ')
    var = input('Enter the variable to differentiate with respect to: ')
    try:
        f = sympify(f)
    except SympifyError:
        print('Invalid input')
    else:
        derivative(f, var)
