from sympy import *
import numpy as np


def estimate(radius, n_darts):

    dart_positions = 2 * np.random.rand(n_darts, 2) - 1  # generates numbers in [-1, 1]

    darts_inside_circle = 0
    for x, y in dart_positions:
        if np.sqrt(x**2 + y**2) < 1:
            darts_inside_circle += 1 # another dart has fallen in the circle

    circle_area = float(pi)*radius**2
    square_area = (2*radius)**2
    estimation = (darts_inside_circle/n_darts) * square_area

    print("Area: {0}, Estimated ({1}): {2}".format(circle_area, n_darts, estimation))


if __name__ == '__main__':
    radius = int(input("Enter the radius: "))
    estimate(radius, 1000)
    estimate(radius, 100000)
    estimate(radius, 1000000)
