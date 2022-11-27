'''
A growing circle
'''
from matplotlib import pyplot as plt
from matplotlib import animation


def create_circle():
    circle = plt.Circle((0, 0), 0.05)
    return circle


''' 
Receive two arguments: 
    - i: frame number that is automatically passed to it when called
    - circle: patch object that we want to update every frame
'''


def update_radius(i, circle):
    circle.radius = i*0.5
    return circle,


def create_animation():
    fig = plt.gcf()
    ax = plt.axes(xlim=(-10, 10), ylim=(-10, 10))
    ax.set_aspect('equal')
    circle = create_circle()
    ax.add_patch(circle)

    '''
    fig: current figure object
    update_radius: function responsable to draw every frame
    fargs: consists of all the arguments to be passed to the update_radius
    frames: number of frames in the animation
    interval: time interval in miliseconds between two frames
    '''
    anim = animation.FuncAnimation(
        fig, update_radius, fargs=(circle,), frames=30, interval=50)
    plt.title('Simple Circle Animation')
    plt.show()


if __name__ == '__main__':
    create_animation()
