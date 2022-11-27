def is_even(n):
    
    if n % 2 == 0:
        return True
    else:
        return False

def show_numbers(n):
    
    if is_even(n):
        print('Even')
        for i in range(int(n), int(n)+19):
            if is_even(i):
                print(i)
    else:
        print('Odd')
        for i in range(int(n), int(n)+19):
            if is_even(i) != True:
                print(i)


if __name__ == '__main__':

    n = float(input('Your number pls: '))

    if n.is_integer():
        show_numbers(n)
    
    else:
        print('Your number must be an integer.')