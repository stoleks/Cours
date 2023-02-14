# -*- coding: utf-8 -*-
"""
  Trace les modes de vibration d'une corde
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# x : position
# t : temps
# c : célérité
# l : longueur d'onde
def ondeMonochromatique (x, t, l, c):
    k = 2 * np.pi / l
    return np.cos (k*c*t - k*x)

# propriété de la figure
fig = plt.figure ()
plt.xlabel ("Position")
plt.ylabel ("Amplitude")
plt.title ("Onde monochromatique")
plt.axhline (y=0, color='black')
x = np.linspace (0, 1, 1000)


# vitesse de propagation de l'onde
c = 300
# pour l'échelle
plt.plot (x, ondeMonochromatique (x, 0, 0.1, c), color='darkorange')
# animation de l'onde
t = 0
images = 1200
tempsMax = 2/c
dt = tempsMax / images
onde = np.zeros ((images, len (x)))
for i in range(images):
    onde[i, :] = ondeMonochromatique (x, t, 0.2, c)
    t += dt

# animation
line, = plt.plot ([], [], 'darkorange', linewidth=2)
def animate (i):
    line.set_data (x, onde[i, :])
    return line,
anim = animation.FuncAnimation (fig, animate, frames=images, interval=1, blit=True, repeat=True)
plt.show ()
