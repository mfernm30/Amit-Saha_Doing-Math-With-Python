from sympy import sympify
from sympy.core.sympify import SympifyError

#When user enter an invalid input sympify sends an error.
expr = input('Enter a mathematical expression: ')
expr = sympify(expr)

#We can import SympifyError and catch de exception to view the correct error.
try:
    expr = sympify(expr)
except SympifyError:
    print('Invalid input')