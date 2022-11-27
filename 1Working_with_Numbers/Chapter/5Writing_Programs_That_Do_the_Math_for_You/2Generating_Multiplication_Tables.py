"""

    Format method works like this:
    item1 = 'apples'
    item2 = 'bananas'
    item3 = 'grapes'
    print('At the grocery store, I bought some {0} and {1} and {2}'.format(item1, item2, item3))


    '{0}'.format(1.25456)
    '{0:.2f}'.format(1.25456) Especify number of decimals.
    '{0:.2f}'.format(1.25556) The number will be rounded.   
    '{0:.2f}'.format(1)

"""

'''
    Multiplication table printer
'''

def multi_table(a):
    for i in range(1, 11):
        print('{0} x {1} = {2}'.format(a, i, a*i))

if __name__ == '__main__':
    a = input('Enter a number: ')
    multi_table(float(a))
