import matplotlib as mp
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as pl


# Parameters
a = 1.0
b = 0.8
wavelength   = 1.   # length of each turn
Nturns       = 5    # number of helices' turns
Npoints      = 1e3  # number of points in the curves


# Derived parameters
t = np.linspace(0, wavelength*Nturns, int(Npoints) )
omega = 2*np.pi/wavelength
theta = wavelength*1.2


# Curves
x1 = a*np.sin(omega*t)
y1 = b*np.cos(omega*t)

x2 = a*np.sin(omega*t + theta)
y2 = b*np.cos(omega*t + theta)


# Interactive plotting
fig = pl.figure()
ax = fig.gca(projection='3d')
ax.plot(x1, y1, t, '-b', lw=4)
ax.plot(x2, y2, t, '-b', lw=4)
ax.set_xlim([-3,3])
ax.set_ylim([-3,3])

pl.show()

