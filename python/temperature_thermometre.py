import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


# fonction lineaire y = a*x
def lineaire (x, a, b):
    return a*x + b

T = [32.0, 34.5, 37.0, 39.5, 42.0]
U = [50.0, 112.0, 163.5, 205.5, 242.0]
Unorm = []
for tension in U:
    Unorm.append (tension / 2)

# calcul du coefficient directeur
params, covar = curve_fit (lineaire, Unorm, T)
modele = []

for tension in Unorm:
  modele.append (lineaire (tension, *params))
  
plt.plot (Unorm, T, "+", markersize = 15., markeredgewidth = 2.)
plt.plot (Unorm, modele, label ="$T =$ {:.2f} U + {:.2f}".format(*params), color = "green")
plt.xlabel ("U")
plt.ylabel ("T")
plt.legend ()

print(lineaire (100, *params))
print (Unorm)