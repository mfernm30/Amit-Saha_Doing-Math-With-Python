from sympy import Poly, sympify, SympifyError, Symbol, solve_poly_inequality, solve_rational_inequalities, solve_univariate_inequality, sin

'''
-x**2 + 4 < 0
((x-1)/(x+2)) > 0
sin(x) - 0.6 > 0
'''
def solve_polynomial(expr):
    x = Symbol('x')
    ineq_obj = expr
    lhs = ineq_obj.lhs
    p = Poly(lhs, x)
    rel = ineq_obj.rel_op
    return solve_poly_inequality(p, rel)

def solve_rational(expr):
    x = Symbol('x')
    ineq_obj = expr
    lhs = ineq_obj.lhs
    numer, denom = lhs.as_numer_denom()
    p1 = Poly(numer)
    p2 = Poly(denom)
    rel = ineq_obj.rel_op
    return solve_rational_inequalities([[((p1, p2), rel)]])

def solve_univariate(expr):
    x = Symbol('x')
    ineq_obj = expr
    solve_univariate_inequality(ineq_obj, x, relational=False)

if __name__=='__main__':

    expr = input('Enter your inequality: ')
    try:
        exprSympy = sympify('sin(x)-0.6')       
    except SympifyError:
        print('Invalid input')
    else:      
        if(exprSympy.is_polynomial()):
            print(solve_polynomial(expr))
        elif(exprSympy.is_rational_function()):
            print(solve_rational(expr))
        else:
            print(solve_univariate(expr))
