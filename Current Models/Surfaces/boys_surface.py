# A Boy's Surface, brought to you by PharaohCola13

import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.pyplot as plt
from matplotlib import *
from numpy import *
from mpl_toolkits.mplot3d.art3d import *
from matplotlib.animation import *
from fractions import Fraction

name = "Boy's Surface"

def shape(fig, alpha, color, edge_c, edge_w, grid, sides,
				   edges, multi_pi, radius):
# Definition of x
    def x_(u, v):
        x = (cos(u) * (Fraction(1,3) * sqrt(2) * cos(u) * cos(2 * v) + Fraction(2,3) * sin(u) * cos(v))) / (1 - sqrt(2) * sin(u) * cos(u) * sin(3 * v))
        return x

# Definition of y
    def y_(u, v):
        y = (cos(u) * (Fraction(1,3) * sqrt(2) * cos(u) * sin(2 * v) - Fraction(2,3) * sin(u) * sin(v))) / (1 - sqrt(2) * sin(u) * cos(u) * sin(3 * v))
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
    ax = p3.Axes3D(fig)
    ax.set_facecolor('black')  # Figure background turns black

# Axis Properties
    plt.axis(grid)  # Turns off the axis grid
    plt.axis('equal')

# Axis Limits
    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 1)
    ax.set_zlim(-1, 1)

# Surface Plot
    boys_surf = ax.plot_surface(x, y, z)

    boys_surf.set_alpha(alpha)  # Transparency of figure
    boys_surf.set_edgecolor(edge_c)  # Edge color of the lines on the figure
    boys_surf.set_linewidth(edge_w)  # Line width of the edges
    boys_surf.set_facecolor(color)  # General color of the figure
