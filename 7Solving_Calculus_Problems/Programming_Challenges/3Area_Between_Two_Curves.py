'''
Area Between Two Curves

Your challenge here is to write a program that will allow the user to
input any two single-variable functions of x and print the enclosed area
between the two.
'''
from sympy import Integral, Symbol


def enclosed_area(f1, f2, x1, x2):
    x = Symbol('x')
    f1_area = Integral((f1), (x, x1, x2)).doit()
    f2_area = Integral((f2), (x, x1, x2)).doit()
    return (f1_area-f2_area)


if __name__ == '__main__':
    print('Enclosed area between two points')
    fx1 = input('Enter a function of x(Upper function): ')
    fx2 = input('Enter a function of x(Lower function): ')
    x1 = input('Enter x_1 value: ')
    x2 = input('Enter x_2 value: ')
    print("The area between {0}, {1} is {2}".format(
        x1, x2, enclosed_area(fx1, fx2, x1, x2)))
