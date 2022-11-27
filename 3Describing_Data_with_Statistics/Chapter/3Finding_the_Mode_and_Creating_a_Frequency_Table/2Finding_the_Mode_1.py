from collections import Counter

'''
Calculating the mode
'''
def calculate_mode(numbers):
    c = Counter(numbers)
    mode = c.most_common(1)
    return mode[0][0]

def calculate_mode_2(numbers):
    number_of_times = 0
    number = 0
    for i in numbers:
        #print(numbers.count(i), number_of_times) 
        if numbers.count(i) >= number_of_times:
            number_of_times = numbers.count(i)
            number = i
    return number

if __name__=='__main__':
    scores = [7, 8, 9, 2, 10, 9, 9, 9, 9, 4, 5, 6, 1, 5, 6, 7, 8, 6, 1, 10]
    mode = calculate_mode(scores)
    print('First method: The mode of the list of numbers is: {0}'.format(mode))
    print('Second method: The mode of the list of numbers is: {0}'.format(calculate_mode_2(scores)))