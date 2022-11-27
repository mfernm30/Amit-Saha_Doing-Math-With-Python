from fractions import Fraction

a = Fraction(input('Enter a fraction: '))

# Handling ZeroDivisionError 3/0 
try:
    a = Fraction(input('Enter a fraction: '))
except ZeroDivisionError:
    print('Invalid fraction')

z = complex(input('Enter a complex number: '))
print(z)
# Si metemos un número complejo con espacios da error, controlar mediante ValueErrorException
