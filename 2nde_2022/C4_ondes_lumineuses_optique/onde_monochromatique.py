# -*- coding: utf-8 -*-
"""
  Trace les modes de vibration d'une corde
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# n : ordre
# c : célérité
# L : longueur de la corde
def modePropre (x, t, n, c, L):
    k = np.pi * n / L
    return np.cos (k*c*t - k*x)

# propriété de l'onde
c = 500
L = 1

# propriété de la figure
fig = plt.figure ()
plt.xlabel ("$x / L$")
plt.ylabel ("$y(x, t) / y_{max}$")
plt.title ("Troisième mode propre d'une corde")

# tracé des 4 premiers modes
x = np.linspace (0, L, 1000)
plt.plot (x / L, 2*modePropre (x, 0, 2, c, L), label=r"$y_3(x, 0)$", linewidth=5, color='white')
plt.axhline (y=0, color='black')


"""
animation du mode
"""
# calcul du mode
t = 0
images = 1200
tempsMax = 2/c
dt = tempsMax / images
onde = np.zeros ((images, len (x)))
for i in range(images):
    onde[i, :] = modePropre (x, t, 100, c, L)
    #for j in range (1, 50, 10):
    #    onde[i, :] += modePropre (x, t, j, c, L)
    t += dt

# animation
line, = plt.plot ([], [], 'darkorange', linewidth=2)
def animate (i):
    line.set_data (x, onde[i, :])
    return line,
anim = animation.FuncAnimation (fig, animate, frames=images, interval=1, blit=True, repeat=True)

plt.show ()