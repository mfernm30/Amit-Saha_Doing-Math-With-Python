from pylab import plot, show

x_numbers = [1, 2, 3]
y_numbers = [2, 4, 6]

# If we specify = it means that dots will be connected with a line
# Several marker options like 'o', '*', 'x', '+'
plot(x_numbers, y_numbers, marker = 'o')
show()
plot(x_numbers, y_numbers, 'o')
show()
plot(x_numbers, y_numbers, '*')
show()
plot(x_numbers, y_numbers, 'x')
show()
plot(x_numbers, y_numbers, '+')
show()