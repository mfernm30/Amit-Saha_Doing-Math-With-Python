'''
Example of using matplotlib's Circle patch
'''
import matplotlib.pyplot as plt


def create_circle():
    # ec='r', fc='g' to change edge and main color
    circle = plt.Circle((0, 0), radius=0.5)
    return circle


def show_shape(patch):
    ax = plt.gca()
    ax.add_patch(patch)
    # Set the ratio of the length of the x- and y-axes to 1:1
    ax.set_aspect('equal')
    plt.axis('scaled')
    plt.show()


if __name__ == '__main__':
    c = create_circle()
    show_shape(c)
