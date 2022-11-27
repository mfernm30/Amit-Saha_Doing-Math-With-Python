'''
    You learned about the factor() function, which prints the factors of an 
    expression. Now that you know how your program can handle expressions 
    input by a user, write a program that will ask the user to input an expres-
    sion, calculate its factors, and print them. Your program should be able to 
    handle invalid input by making use of exception handling.
'''


from sympy import Symbol, sympify, factor, SympifyError

if __name__=='__main__':

    expr = input('Enter your expression: ')
    
    try:
        expr = sympify(expr)       
    except SympifyError:
        print('Invalid input')
    else:      
        print(factor(expr))