# -*- coding: utf-8 -*-
"""
  Trace i_1 en fonction de i_2 et calcul le coefficient directeur
"""

# bibliotheque contenant des fonctions predefinies
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# fonction lineaire y = a*x
def lineaire (x,a):
    return a*x

# donnees mesurees
i1 = []
i2 = []

# calcul du coefficient directeur
params, covar = curve_fit (lineaire, i1, i2)
modele=[]
for val in i1:
  modele.append (lineaire (val, *params))

# Trace les donnees et le modele lineaire
plt.plot (i1, modele, label ="$i_2 =$ {:.2f} $i_1$".format(*params), color = "green")
plt.plot (i1, i2, "+", markersize = 15., markeredgewidth = 2., label="Points experimentaux", color = "red")

# Titre axes et legende du graphique
plt.legend()
plt.title ("Refraction")
plt.xlabel ("Angle d'incidence $i_1$")
plt.ylabel ("Angle de refraction $i_2$")
plt.grid ()

# Affiche le graphique
plt.show()
