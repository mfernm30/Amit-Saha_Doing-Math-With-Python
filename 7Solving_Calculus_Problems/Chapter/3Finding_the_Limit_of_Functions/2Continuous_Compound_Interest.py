from sympy import Limit, Symbol, S

# When n increases the continuous compound interest approaches the value of e
n = Symbol('n')
print(Limit((1+1/n)**n, n, S.Infinity).doit())

# For any amount of p at any rate r and any number of years t
p = Symbol('p', positive=True)
r = Symbol('r', positive=True)
t = Symbol('t', positive=True)
print(Limit(p*(1+r/n)**(n*t), n, S.Infinity).doit())
