from sympy.plotting import plot
from sympy import Symbol

x = Symbol('x')
plot(2*x+3)

#Changing the range of the plot shown.
plot((2*x + 3), (x, -5, 5))

#Using show=False parameter for not displaying the plot till the programmer wants.
p = plot(2*x + 3, (x, -5, 5), title='A Line', xlabel='x', ylabel='2x+3', show=True)
