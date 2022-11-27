'''
Run until exit layout

def fun():
    print('I am in an endless loop')

if __name__ == '__main__':
    while True:
        fun()
        answer = input('Do you want to exit? (y) for yes ')
        if answer == 'y':
            break
'''

'''
    Multiplication table printer with exit power.
'''

def multi_table(a, n):
    for i in range(1, int(n+1)):
        print('{0} x {1} = {2}'.format(int(a), i, int(a*i)))

if __name__ == '__main__':
    
    while True:
        a = float(input('Enter a number: '))
        n = float(input('Enter number of multiples you want to see: '))
        
        if a.is_integer() and n.is_integer():
            multi_table(a, n)
        else:
            print('Error, the number and the number of multiples must be integers.')
        
        answer = input('Do you want to exit? (y) for yes ')
        if answer == 'y':
            break
