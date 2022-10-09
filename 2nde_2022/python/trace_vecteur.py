
# import des bibliothèques utilisées
import numpy as np
import matplotlib.pyplot as plt


# dessine une flèche partant d'un point (x1, y1) et allant à un point (x2, y2)
def traceFleche (base, tete, largeur=1, couleur='c') :
    taille = 0.025 * largeur
    plt.arrow (base[0], base[1], tete[0], tete[1],
               shape='full', lw=largeur, head_width=taille, color=couleur)


# dessine les points associés aux coordonnées (x, y)
def tracePoints (x, y) :
    plt.scatter (x, y)    
    

# x et y sont des listes contenant les coordonnées , i le numéro du point
# dont on affiche la vitesse, Dt l’intervalle de temps entre chaque point
def vitesse (x, y, Dt, i) :
    # tracé du vecteur vitesse
    xMoyen = (x[i + 1] - x[i - 1]) / 4
    yMoyen = (y[i + 1] - y[i - 1]) / 4
    #plt.annotate (str(Dt * i) + 's', xy=(x[i] + 0.25, y[i]))
    traceFleche ((x[i], y[i]), (xMoyen, yMoyen))
    

# definition d'une liste de coordonnées et d'un pas de temps
def trajectoireX (t, v) :
    return v * t
def trajectoireY (t, v) :
    return (v * t) - 9.81*(t**2 / 2) + 1.8
v = 5
points = 20
tMax = 1.5
Dt = tMax / points
t = np.linspace (0, tMax, points)
x = trajectoireX (t, v)
y = trajectoireY (t, v)
    

# tracé des points repérés
tracePoints (x, y)

# tracé des vitesses
for i in range(1, points - 1):
    vitesse (x, y, Dt, i)

# afffichages des axes et des grandeurs tracés
plt.xlabel (r'$x [m]$')
plt.ylabel (r'$y [m]$')
plt.title ("Trajectoire d'une balle lancée")
plt.show()