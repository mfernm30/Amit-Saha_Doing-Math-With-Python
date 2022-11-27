import csv
import random
from sympy import FiniteSet
from matplotlib_venn import venn2
import matplotlib.pyplot as plt

def write_csv():
    data_IDs = [*range(0,21)]

    with open('sports.csv', 'w', encoding='UTF8') as f:
        # write the header
        f.write("StudentID, Football, Others")
        
        # write data
        for id in data_IDs:
            if id !=20:
                f.write("{0},{1},{2}{3}".format(id,random.randint(0, 1), random.randint(0, 1),"\n"))
            else:
                f.write("{0},{1},{2}".format(id,random.randint(0, 1), random.randint(0, 1)))


def read_csv(filename):
    football = []
    others = []

    with open(filename) as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            if row[1] == '1':
                football.append(row[0])
            if row[2] == '1':
                others.append(row[0])

    return football, others

def draw_venn(sets):
    venn2(subsets=sets, set_labels=('Football', 'Others'))
    plt.show()

if __name__ == '__main__':
    write_csv()
    results = read_csv("sports.csv")
    s1 = FiniteSet(*results[0])
    s2 = FiniteSet(*results[1])
    draw_venn([s1, s2])
