from sympy import *
import numpy as np


def estimate(n_darts):

    # generates numbers in [-1, 1]
    dart_positions = 2 * np.random.rand(n_darts, 2) - 1

    darts_inside_circle = 0
    for x, y in dart_positions:
        if np.sqrt(x**2 + y**2) < 1:
            darts_inside_circle += 1  # another dart has fallen in the circle

    estimation = 4*(darts_inside_circle/n_darts)

    print("Estimated PI(Number of darts: {0}): {1}".format(
        n_darts, estimation))


if __name__ == '__main__':
    print("Assuming any value for the radius")
    estimate(1000)
    estimate(100000)
    estimate(1000000)
    estimate(5000000)
