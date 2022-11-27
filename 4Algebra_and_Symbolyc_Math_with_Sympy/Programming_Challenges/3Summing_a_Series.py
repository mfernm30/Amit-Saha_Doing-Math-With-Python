'''
    This program finds the sum of an arbitrary series when the user
    supply the nth term of the series and the number of terms in it.
'''
from sympy import Symbol, sympify, solve, SympifyError, summation, pprint

if __name__=='__main__':

    expr = input('Enter the nth term: ')
    range = input('Enter the number of terms: ')

    try:
        n = Symbol('n')
        expr = sympify(expr) 
        s = summation(expr, (n, 1, range))          
    except SympifyError:
        print('Invalid input')
    else:      
        pprint(s)