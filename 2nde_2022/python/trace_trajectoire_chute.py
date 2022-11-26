import numpy as np # bibliothèque de calcul
import matplotlib.pyplot as plt # blibliothèque d'affichage

# dessine une flèche partant du point 'départ' et allant au point 'fin'
def traceFleche (depart, fin) :
    taille = 0.1 # taille de la pointe de la flêche
    plt.arrow (depart[0], depart[1], fin[0], fin[1], # coordonnées du vecteur
               head_length=taille, head_width=taille) # apparence du vecteur

# calcul et trace le vecteur vitesse
def traceVecteurVitesses (x, y, Dt) :
    for i in range (1, len (x) - 1) :
        vx = (x[i + 1] - x[i - 1]) / 2*Dt
        vy = (y[i + 1] - y[i - 1]) / 2*Dt
        traceFleche ((x[i], y[i]), (vx, vy))

# calcul de la trajectoire selon x et y
def trajectoireX (t, v, alpha) :
    cosinusAlpha = np.cos (alpha * np.pi/180)
    return v * t * cosinusAlpha
def trajectoireY (t, v, alpha) :
    sinusAlpha = np.sin (alpha * np.pi/180)
    return 2 + (v * t)*sinusAlpha - 4.9*(t**2)

# affichage d'une trajectoire
def trajectoire (t, v, alpha) :
    # calcul des positions x et y
    x = trajectoireX (t, v, alpha)
    y = trajectoireY (t, v, alpha)
    # tracé des points repérés
    plt.plot (x, y, 'o', label='Angle = ' + str(alpha))
    # tracé des vitesses
    traceVecteurVitesses (x, y, max (t) / 2)

# réglage du graphique
plt.axis('equal') # pour avoir des vecteurs symétriques
plt.xlabel (r'$x$ (en cm)') # légende de l'abscisse
plt.ylabel (r'$y$ (en cm)') # légende de l'ordonnée
plt.title ("Trajectoire d'une balle lancée") # titre du graphique
plt.xlim (0, 11) # limite du graphique selon x
plt.ylim (0.1, 6) # limite du graphique selon y

# vitesse initiale
v = 10
points = 50
# calcul de l'échelle de temps
tMax = 3
t = tMax / (points - 1)
t = np.linspace (0, tMax, points)

# calcul de la trajectoire pour différents angles
for alpha in range (20, 70, 10) :
    trajectoire (t, v, alpha)
plt.plot (np.linspace (0, 0, 100), color='black')
plt.legend () # affichage de la légende des courbes
plt.show () # affichage du graphique