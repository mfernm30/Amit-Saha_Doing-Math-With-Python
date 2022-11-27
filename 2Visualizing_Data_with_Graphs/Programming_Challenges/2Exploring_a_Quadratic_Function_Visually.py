'''
Quadratic function calculator
'''

from pylab import plot, show, title, xlabel, ylabel

# Assume values of x
x_values = range(-1, 9)
y_values = []
for x in x_values:
    # Calculate the value of the quadratic function
    y = x**2 + 2*x + 1
    y_values.append(y)
    print('x={0} y={1}'.format(x, y))

plot(x_values, y_values, marker = 'o')
title('Función cuadrática')
xlabel('Valores de x')
ylabel('Valores de y')   
show()