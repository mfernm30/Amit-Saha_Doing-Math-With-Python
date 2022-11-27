from collections import Counter
import csv

'''
Calculating the mean
'''
def calculate_mean(numbers):
    s = sum(numbers)
    N = len(numbers)
# Calculate the mean
    mean = s/N
    return mean

'''
Calculating the median
'''
def calculate_median(numbers):
    
    N = len(numbers)
    numbers.sort()
    # Find the median
    if N % 2 == 0:
        # if N is even
        m1 = N/2
        m2 = (N/2) + 1
        # Convert to integer, match position
        m1 = int(m1) - 1
        m2 = int(m2) - 1
        median = (numbers[m1] + numbers[m2])/2
    else:
        m = (N+1)/2
        # Convert to integer, match position
        m = int(m) - 1
        median = numbers[m]
    return median

'''
Calculating the mode
'''
def calculate_mode(numbers):
    c = Counter(numbers)
    mode = c.most_common(1)
    return mode[0][0]

'''
Find the variance of a list of numbers
'''    
def calculate_variance(numbers):
    # Find the list of differences
    mean = calculate_mean(numbers)
    # Find the differences from the mean
    diff = []
    for num in numbers:
        diff.append(num-mean)
    # Find the squared differences
    squared_diff = []
    for d in diff:
        squared_diff.append(d**2)
    # Find the variance
    sum_squared_diff = sum(squared_diff)
    variance = sum_squared_diff/len(numbers)
    return variance

'''
Find the standard deviation of a list of numbers
'''
def calculate_std_deviation(numbers):
    return calculate_variance(numbers)**0.5

'''
Read from a CSV file a list of numbers
'''
def read_csv(filename):
    numbers = []
    with open(filename) as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            numbers.append(int(row[0]))
    return numbers

if __name__ == '__main__':
    numbers = read_csv('numbers.csv')
    print(calculate_std_deviation(numbers))