from sympy import Integral, Symbol, Derivative, sqrt, sympify


def distance(a, b, f):
    x = Symbol('x')
    df = Derivative(f, x).doit()
    i = sqrt(1 + ((df)**2))

    return Integral((i), (x, a, b)).doit().evalf()


if __name__ == '__main__':
    f = input('Enter a function in one variable: ')
    a = input('Enter the starting point of the cycling path: ')
    b = input('Enter the finish point of the cycling path: ')
    try:
        f = sympify(f)
    except SympifyError:
        print('Invalid function entered')
    else:
        print("Distance you cycled between {0}, {1} is {2}".format(
            a, b, distance(a, b, f)))
