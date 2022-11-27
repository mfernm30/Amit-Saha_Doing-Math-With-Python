'''
Drawing the Hénon map
'''
import matplotlib.pyplot as plt
import random


def transformation_1(p):

    x = p[0]
    y = p[1]
    x1 = 1 - (1.4*(x**2)) + y
    y1 = 0.3*x
    return x1, y1


def get_index(probability):
    r = random.random()
    c_probability = 0
    sum_probability = []
    for p in probability:
        c_probability += p
        sum_probability.append(c_probability)
    for item, sp in enumerate(sum_probability):
        if r <= sp:
            return item
    return len(probability)-1


def transform(p):
    # List of transformation functions
    transformations = [transformation_1]
    probability = [1]
    # Pick a random transformation function and call it
    tindex = get_index(probability)
    t = transformations[tindex]
    x, y = t(p)
    return x, y


def draw_henon(n):
    # We start with (0, 0)
    x = [0]
    y = [0]
    x1, y1 = 1, 1
    for i in range(n):
        x1, y1 = transform((x1, y1))
        x.append(x1)
        y.append(y1)
    return x, y


if __name__ == '__main__':
    n = int(input('Enter the number of points in the Hénon map: '))
    x, y = draw_henon(n)
    # Plot the points
    plt.plot(x, y, 'o')
    plt.title('Hénon map with {0} points'.format(n))
    plt.show()
