'''
    Multiplication table printer
'''

def multi_table(a, n):
    for i in range(1, int(n+1)):
        print('{0} x {1} = {2}'.format(int(a), i, int(a*i)))

if __name__ == '__main__':
    
    a = float(input('Enter a number: '))
    n = float(input('Enter number of multiples you want to see: '))
    
    if a.is_integer() and n.is_integer():
        multi_table(a, n)
    else:
        print('Error, the number and the number of multiples must be integers.')
