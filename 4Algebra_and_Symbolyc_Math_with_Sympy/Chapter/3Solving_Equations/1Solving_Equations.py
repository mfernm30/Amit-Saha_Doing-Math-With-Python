from sympy import Symbol, solve 

#Use solve to solve the expression. The result assume that the expression is equal 0.
x = Symbol('x')
expr = x - 5 - 7

print(solve(expr))