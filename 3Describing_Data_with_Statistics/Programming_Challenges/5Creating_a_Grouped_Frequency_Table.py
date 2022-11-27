import csv

'''
Create the frequency group table classes.
Example of grades frecuency (page 69):
    Grade   Frequency
    1–6     6
    6–11    14
'''
def create_classes(numbers, n):
    low = min(numbers)
    high = max(numbers)
    # Width of each class
    width = (high - low)/n
    classes = []
    a = low
    b = low + width
    classes = []
    while a < (high-width):
        classes.append((a, b))
        a = b
        b = a + width
    # The last class may be of a size that is less than width
    classes.append((a, high+1))
    return classes

'''
Calculate frequencies for n classes
'''
def calculate_frequencies(data, n_classes, classes):
    frequencies = [0] * n_classes
    c = 0
    for x in classes:
        for d in data:
            if d>=x[0] and d<x[1]:
                frequencies[c] = frequencies[c] + 1
        c = c + 1
    return frequencies
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

'''
Print the frequency group table
'''
def print_class_frecuency_table(data, n_classes):
    classes = create_classes(data, n_classes)    
    frecuencies = calculate_frequencies(data, n_classes, classes)
    print('Classes \t Frecuencies')
    for c, f in zip(classes, frecuencies):
        print(str(c) + '\t ' + str(f))

if __name__ == '__main__':
    data = read_csv('grades.csv')
    n_classes = int(input('Introduce el número de clases:'))
    print_class_frecuency_table(data, n_classes)