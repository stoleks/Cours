# -*- coding: utf-8 -*-
"""
  Trace sin(i_1) en fonction de sin(i_2) et calcul le coefficient directeur
"""

# bibliotheque contenant des fonctions predefinies
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# convertit les degres en radian
def enRadian (angleEnDegre):
  return angleEnDegre * np.pi / 180

# fonction lineaire y = a*x
def lineaire (x,a):
    return a*x

# donnees mesurees
i1 = [0, 5]
i2 = []
sini1 = []
sini2 = []

# calcul des sinus
for i in range (len (i1)):
    sini1.append (np.sin (enRadian (i1[i])))
    sini2.append (np.sin (enRadian (i2[i])))

# calcul du coefficient directeur
params, covar = curve_fit (lineaire, sini1, sini2)
modele=[]
# On ajoute 1 pour que le modele aille plus loin que les points experimentaux
x = sini1 + [1]
for val in x:
  modele.append (lineaire (val, *params))
  
# Trace les donnees et le modele lineaire
plt.plot (x, modele, label ="$\sin (i_2) =$ {:.2f} $\sin (i_1)$".format(*params), color = "green")
plt.plot (sini1, sini2, "+", markersize = 15., markeredgewidth = 2., label="Points experimentaux", color = "red")

# Titre axes et legende du graphique
plt.legend()
plt.title ("Refraction")
plt.xlabel ("$\sin (i_1)$")
plt.ylabel ("$\sin (i_2)$")
plt.grid ()

# Affiche le graphique
plt.show()