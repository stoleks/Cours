# -*- coding: utf-8 -*-
"""
  Courbe d'étalonnage de la concentration en sucre en fonction de la masse volumique
"""

# bibliotheque contenant des fonctions predefinies
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


# fonction lineaire y = a*x
def lineaire (x, a, b):
    return a*x + b

# donnees mesurees
concentration = [0.01, 0.01, 0.02, 0.03, 0.04, 0.04, 0.05, 0.06, 0.06, 0.07, 0.08, 0.09, 0.09, 0.11, 0.01, 0.03, 0.04]
masseVolumique = [1.0, 0.99, 1.03, 1.03, 1.03, 1.03, 1.03, 1.04, 1.04, 1.05, 1.08, 1.07, 1.08, 1.09, 0.99, 1.01, 1.03]

# calcul du coefficient directeur
params, covar = curve_fit (lineaire, concentration, masseVolumique)
modele=[]
# On ajoute 1 pour que le modele aille plus loin que les points experimentaux
for c in concentration:
  modele.append (lineaire (c, *params))

# Trace les donnees et le modele lineaire
plt.plot (concentration, modele, color = "green")
plt.plot (concentration, masseVolumique, "+", markersize = 15., markeredgewidth = 2., label="Points experimentaux", color = "red")

# Titre axes et legende du graphique
plt.legend()
plt.title ("Masse volumique de l'eau sucrée en fonction de la concentration en sucre")
plt.xlabel ("Concentration")
plt.ylabel ("Masse volumique")
plt.grid ()

# Affiche le graphique
plt.show()