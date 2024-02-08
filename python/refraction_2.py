# -*- coding: utf-8 -*-
"""
  Trace sin(i1) en fonction de sin(i2) et calcul le coefficient directeur
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
i1 = [0., 5., 10., 15., 20., 30., 40., 50., 60., 70.]
i2 = [0, 3.3, 6.7, 9.9, 13.2, 19.5, 25.4, 30.7, 35.3, 38.8]
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