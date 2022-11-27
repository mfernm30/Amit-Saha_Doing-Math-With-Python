'''
    Plot 2 expressions given as an input by the user.
    Then print the solution of the expression.
'''


from sympy import Symbol, sympify, solve, plot, SympifyError

def plot_expression(expr):
    y = Symbol('y')
    solutions = solve(expr, y)
    expr_y = solutions[0]
    plot(expr_y)

if __name__=='__main__':

    expr1 = input('Enter your first expression in terms of x and y: ')
    expr2 = input('Enter your second expression in terms of x and y: ')
    
    try:
        expr1 = sympify(expr1)
        expr2 = sympify(expr2)           
    except SympifyError:
        print('Invalid input')
    else:      
        #Plotting expressions
        plot_expression(expr1)
        plot_expression(expr2)
        #Print the solution
        print(solve(expr1, dict=True))
        print(solve(expr2, dict=True))