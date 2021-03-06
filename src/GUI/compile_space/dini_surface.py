# A Dini's Surface, brought to you by PharaohCola13

import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.pyplot as plt

from mpl_toolkits.mplot3d.art3d import *
from matplotlib.animation import *
from matplotlib import *
from numpy import *

name = "Dini's Surface"

def shape(fig, alpha, color, edge_c, edge_w, grid, sides, edges, multi_pi, radius, height):
    # Definition of x
    def x_(u, v):
        x = a * cos(u) * sin(v)
        return x

    # Definition of y
    def y_(u, v):
        y = a * sin(u) * sin(v)
        return y


    # Definition of z
    def z_(u, v):
        z = -1 * (a * (cos(v) + log1p(tan(v/2))) + (b * u))
        return z

    a = radius # Radius
    b = height # Height

    # Value of the angles
    u = linspace(0, 3 * pi, 50)
    v = linspace(0, pi, 50)

    u, v = meshgrid(u, v)

    # Symbolic representation
    x = x_(u, v)
    y = y_(u, v)
    z = z_(u, v)

    # Figure Properties
    ax = p3.Axes3D(fig)
    ax.set_facecolor('black')  # Figure background turns black

    # Axis Properties
    plt.axis(grid)  # Turns off the axis grid
    plt.axis('equal')

    # Axis Limits
    ax.set_xlim(-2, 2)
    ax.set_ylim(-2, 2)
    ax.set_zlim(-4 *pi, 2 *pi)

    # Surface Plot
    dini = ax.plot_surface(x, y, z)

    dini.set_alpha(alpha)  # Transparency of figure
    dini.set_edgecolor(edge_c)  # Edge color of the lines on the figure
    dini.set_linewidth(edge_w)  # Line width of the edges
    dini.set_facecolor(color)  # General color of the figure
