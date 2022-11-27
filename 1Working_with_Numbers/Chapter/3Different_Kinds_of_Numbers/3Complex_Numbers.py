a = 2 + 3j
print(type(a))
print(a)

a = complex(2, 3)
print(a)

# Operations with complex numbers

b = 3 + 3j
print(a + b)
print(a - b)
print(a * b)
print(a / b)

# % and // operations are not valid for complex numbers

# We can retrieve real and imaginary part of a complex number with real and imag attributes

z = 2 + 3j

print(z.real)
print(z.imag)

# Conjugate, same real part but an imaginary part with an equal magnitude but opposite sign

print(z.conjugate())

# To calculate the magnitude of a complex number use the formula

magnitude = (z.real ** 2 + z.imag ** 2) ** 0.5
print(magnitude)

# With abs we can calculate the absolute value of a number, or the magnitude of a complex number

print(abs(-5))
print(abs(5))
print(abs(magnitude))