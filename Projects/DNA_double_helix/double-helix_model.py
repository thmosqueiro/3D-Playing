import matplotlib as mp
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as pl


# In[115]:

# Parameters
a = 1.0
b = 0.8

wavelength   = 1.   # length of each turn
Nturns       = 20   # number of helices' turns
Npoints      = 1e2  # number of points in the curves


# In[116]:

def degrad(x):
    return (x / 180. * np.pi)

# Derived parameters
t = np.linspace(0, wavelength*Nturns, int(Npoints) )
omega = degrad(32.5)/wavelength
theta = wavelength * 1.5
skip  = int(Npoints/Nturns)


# In[117]:

colors = np.random.choice(['red', 'yellow', 'blue', 'black'], Nturns)


# In[118]:

# Curves
x1 = a*np.sin(omega*t)
y1 = b*np.cos(omega*t)

x2 = a*np.sin(omega*t + theta)
y2 = b*np.cos(omega*t + theta)


# Interactive plotting
fig = pl.figure()
ax = fig.gca(projection='3d')
ax.plot(x1, y1, t, '-b', lw=4)
ax.plot(x2, y2, t, '-r', lw=4)

rg = np.arange(Nturns) * skip
dx = (x1 - x2)[rg]
dy = (y1 - y2)[rg]
ax.quiver(x1[rg], y1[rg], t[rg], -dx, -dy, 0, length=.5, color=colors, pivot='tail', lw=3)
ax.quiver(x2[rg], y2[rg], t[rg],  dx,  dy, 0, length=.5, color=colors, pivot='tail', lw=3)
ax.set_xlim([-3,3])
ax.set_ylim([-3,3])

# For some reason, the red curve is always plotted in front of the blue
pl.show()
