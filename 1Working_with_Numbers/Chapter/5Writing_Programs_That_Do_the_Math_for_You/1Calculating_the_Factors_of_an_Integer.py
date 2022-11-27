def is_factor(a, b):
    if b % a == 0:
        return True
    else:
        return False

print(is_factor(4, 1024))

# Example of range range(5) range(1,10,2)
for i in range(1, 4):
    print(i)


'''
Find the factors of an integer
'''

def factors(n):
    for i in range(1,n+1):
        if n % i == 0:
            print(i)

if __name__ == '__main__':

    n = float(input('Your Number Please: '))
    # Cuando sea 3 o 3.0 se realizara el cálculo de sus factores: 3, 3.0 , 3.3, symbol
    # Si el número es positivo y se comporta como un int.
    if n > 0 and n.is_integer():
        factors(int(n))
    else:
        print('Please enter a positive integer')