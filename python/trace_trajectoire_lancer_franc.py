# Pour avoir des modules de calculs et d'affichage
import numpy as np              # calcul
import matplotlib.pyplot as plt # affichage

# calcul de la trajectoire selon x et y
def positionX (v0, alpha, t) : # v0 t cos(alpha)
    return v0 * t * np.cos (alpha * np.pi / 180) 
def positionY (v, alpha, t) :  # -g t² /2 + v0 t sin(alpha)
    return -9.81/2*(t**2) + (v0 * t)*np.sin (alpha * np.pi / 180) 

# Vitesse et angle initial, nombre de points a calculer
v0 = float (input ("Valeur de la vitesse initiale v0 (m/s) = "))
alpha = float (input ("Valeur de l'angle de départ (°) = "))
points = 50

# calcul des positions x et y
x, y = [],[]              # initialisation des positions
deltaT = 2 / (points - 1) # temps entre 2 points
for i in range(points) :  # pour chaque position i
  x.append (positionX (v0, alpha, i * deltaT)) # calcul de l'abscisse en mètre
  y.append (positionY (v0, alpha, i * deltaT)) # calcul de l'ordonnée en mètre
  
# réglage du graphique
plt.xlabel (r"$x$ (en m)")            # légende de l'abscisse
plt.ylabel (r"$y$ (en m)")            # légende de l'ordonnee
plt.title ("Trajectoire de la balle") # titre du graphique
# tracé des points repérés et des vecteur vitesses
plt.plot (x, y, "o", markersize = 5) # affiche des points rond ('o'), taille 4
plt.xlim (0, 5.0)                    # limite du graphique selon x
plt.ylim (0, 2.4)                    # limite du graphique selon y
plt.xticks (np.arange(0, 5.0, 0.5))  # finesse de la grille selon x
plt.yticks (np.arange(0, 2.4, 0.2))  # finesse de la grille selon y
plt.grid ()                          # affichage de la grille
plt.show ()                          # affichage du graphique