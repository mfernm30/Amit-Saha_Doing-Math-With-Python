from sympy import Symbol, solve, Derivative

x = Symbol('x')
f = x**5 - 30*x**3 + 50*x
d1 = Derivative(f, x).doit()

critical_points = solve(d1)

# Critical points
A = critical_points[2]
B = critical_points[0]
C = critical_points[1]
D = critical_points[3]

# Second order derivative
d2 = Derivative(f, x, 2).doit()
print("Critical points: ")
print(d2.subs({x: A}).evalf())
print(d2.subs({x: C}).evalf())
print(d2.subs({x: B}).evalf())
print(d2.subs({x: D}).evalf())

# Calculate global maximun
x_min = -5
x_max = 5
print("Calculate global maximun: ")
print(f.subs({x: A}).evalf())
print(f.subs({x: C}).evalf())
print(f.subs({x: x_min}).evalf())
print(f.subs({x: x_max}).evalf())

# Calculate global minimun
print("Calculate global minimun: ")
print(f.subs({x: B}).evalf())
print(f.subs({x: D}).evalf())
print(f.subs({x: x_min}).evalf())
print(f.subs({x: x_max}).evalf())
