import csv 

def calculate_percentile(data, p):
    #Number of elements
    n = len(data)
    #Sort array of numbers
    data.sort()
    #Calculate i
    i = n*p/100 + 0.5
    if i.is_integer():
        result = data[i]
    else:
        #Parte decimal
        k = int(i)
        #Parte fraccionaria
        f = abs(i) - abs(int(i))
        result = (1-f)*data[k] + f*data[k+1]
    return result

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
    data = read_csv('heights.csv')
    print("Introduce the percentile you want to calculate: ")
    print(calculate_percentile(data, float(input())))