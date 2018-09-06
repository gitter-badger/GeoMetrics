# A Boy's Surface, brought to you by PharaohCola13

import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.pyplot as plt

from mpl_toolkits.mplot3d.art3d import *
from matplotlib.animation import *
from matplotlib import *
from numpy import *

name = "Boy's-Surface"

option = int(input('Run? (0) Yes, (1) No\n>> '))

while option == 0:
# Definition of x
    def x_(u, v):
        x = (cos(u) * ((1/3)*sqrt(2)*cos(u)*cos(2*v) + (2/3) * sin(u) * cos(v))) / (1 - sqrt(2)*sin(u) * cos(u)*sin(3 * v))
        return x

# Definition of y
    def y_(u, v):
        y = (cos(u) * ((1/3)*sqrt(2)*cos(u)*sin(2*v) - (2/3) * sin(u) * sin(v))) / (1 - sqrt(2)*sin(u) * cos(u)*sin(3 * v))
        return y


# Definition of z
    def z_(u, v):
        z = cos(u)**2 / (1 - sqrt(2) * sin(u) * cos(u) * sin(3 * v)) - 1
        return z

# Value of the angles
    u = linspace(0, pi, 75)
    v = linspace(0, pi, 75)

    u, v = meshgrid(u, v)

# Symbolic representation
    x = x_(u, v)
    y = y_(u, v)
    z = z_(u, v)

# Figure Properties
    fig = plt.figure(figsize=(8, 8))

    ax = p3.Axes3D(fig)
    ax.set_facecolor('black')  # Figure background turns black

# Axis Properties
    plt.axis('off')  # Turns off the axis grid
    plt.axis('equal')

# Axis Limits
    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 1)
    ax.set_zlim(-1, 1)

# Surface Plot
    color = str(input('What color is the figure?\n>> '))
    alpha = float(input('How transparent is the figure? (0 to 1)\n>> '))
    boys_surf = ax.plot_surface(x, y, z)

    boys_surf.set_alpha(alpha)  # Transparency of figure
    boys_surf.set_edgecolor('w')  # Edge color of the lines on the figure
    boys_surf.set_linewidth(0.25)  # Line width of the edges
    boys_surf.set_facecolor(color)  # General color of the figure

    rotate = int(input('Rotate the figure? (0) Yes, (1) No.\n>> '))
    if rotate == 0:
# Definitions for animation
        def init():
            return boys_surf,


        def animate(i):
# azimuth angle : 0 deg to 360 deg
# elev = i * n --> rotates object about the xy-plane with a magnitude of n
# azim = i * n --> rotates object around the z axis with a magnitude of n
# For top view elev = 90
# For side view elev = 0

            ax.view_init(elev=-90, azim=i * 4)
            return boys_surf,


# Animate
        ani = FuncAnimation(fig, animate, init_func=init,
                           frames=100, interval=20, blit=False, repeat=True)

        save = int(input('Save the animation? (0) Yes, (1) No.\n>> '))
        if save == 0:
# Saving to Boy's-Surface.mp4

            Writer = writers['ffmpeg']
            writer = Writer(fps=15, bitrate=1800)

            ani.save('../Samples/%s.mp4' % name, writer=writer)
            plt.show() # Shows Figure

        elif save == 1:
            plt.show() # Shows Figure

    elif rotate == 1:
        plt.show()  # Shows Figure
    option = int(input('Run again? (0) Yes, (1) No\n>> '))