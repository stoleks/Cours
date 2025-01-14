import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


# fonction lineaire y = a*x
def lineaire (x, a, b):
    return a*x + b

T = [32.0, 34.5, 37.0, 39.5, 42.0]
U = [512, 1120, 1635, 2055, 2430]
Unorm = []
for tension in U:
    Unorm.append (tension / 2)

# calcul du coefficient directeur
params, covar = curve_fit (lineaire, U, T)
modele = []

for tension in U:
  modele.append (lineaire (tension, *params))

plt.plot (U, T, "+", markersize = 15., markeredgewidth = 2.)
plt.plot (U, modele, label ="$T =$ {:.4f} U + {:.2f}".format(*params), color = "green")
plt.xlabel ("U")
plt.ylabel ("T")
plt.legend ()
plt.show ()

print ("Température", lineaire (1728, *params))