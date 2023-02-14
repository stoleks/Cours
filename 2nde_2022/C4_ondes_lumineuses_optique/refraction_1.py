# -*- coding: utf-8 -*-
"""
  Trace i1 en fonction de i2 et calcul le coefficient directeur
"""

# bibliotheque contenant des fonctions predefinies
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# donnees mesurees
i1 = [0., 5., 10., 15., 20., 30., 40., 50., 60., 70.]
i2 = [, , , , , , , , , ]

# Trace les donnees et le modele lineaire
plt.plot (i1, i2, "+", markersize = 15., markeredgewidth = 2., label="Points experimentaux", color = "red")

# Titre axes et legende du graphique
plt.legend()
plt.title ("Refraction")
plt.xlabel ("Angle d'incidence $i_1$")
plt.ylabel ("Angle de refraction $i_2$")
plt.grid ()

# Affiche le graphique
plt.show()
