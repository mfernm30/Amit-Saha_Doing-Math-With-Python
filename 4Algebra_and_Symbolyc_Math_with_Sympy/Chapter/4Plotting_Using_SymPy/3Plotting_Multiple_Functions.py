from sympy.plotting import plot
from sympy import Symbol

'''
    This doesnt work as the book says.
    This code should plot multiple expressions.
    x = Symbol('x')
    plot(2*x+3, 3*x+1)

    This code should plot multiple expressions with a legend and different plot line colors.
    x = Symbol('x')
    p = plot(2*x+3, 3*x+1, legend = True, show = False)
    p[0].line_color = 'b' 
    p[1].line_color = 'r' 
    p.show()

'''