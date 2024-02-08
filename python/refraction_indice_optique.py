import numpy as np
import matplotlib.pyplot as plt

# Conversion des degrée en radian et inversement
def enDegree (angle):
    return angle * 180 / np.pi

def enRadian (angle):
    return angle * np.pi / 180


x = np.linspace (0.01, enRadian(90), 1000)
plt.plot (enDegree (x), enDegree (np.arcsin (1.5 * np.sin (x))), label='$n_1 > n_2$')
plt.plot (enDegree (x), enDegree (np.arcsin (np.sin (x))), label='$n_1 = n_2$')
plt.plot (enDegree (x), enDegree (np.arcsin (0.5 * np.sin (x))), label='$n_1 < n_2$')
plt.xlabel ("Angle incident $i_1$")
plt.ylabel ("Angle réfracté $i_2$")
plt.xlim (0, 90)
plt.ylim (0, 90)
plt.legend ()