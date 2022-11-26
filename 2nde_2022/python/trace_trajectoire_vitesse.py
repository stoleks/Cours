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

# réglage du graphique
plt.axis('equal') # pour avoir des vecteurs symétriques
plt.xlabel (r'$x$ (en cm)') # légende de l'abscisse
plt.ylabel (r'$y$ (en cm)') # légende de l'ordonnée
plt.title ("Trajectoire d'une goutte d'encre") # titre du graphique

# définition de la trajectoire
Dt = 5
x = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
y = [0.02, 0.04, 0.16, 0.32, 0.64, 1.28, 1.96, 2.56, 3.20, 3.84, 3.84, 3.84, 3.84, 0, 0, 0, 0, 0]

# trace les positions et les vecteurs vitesses
plt.plot (x, y, 'go') # g : vert (green), o : cercle
traceVecteurVitesses (x, y, Dt) # trace les vitesses
plt.show () # affiche le graphique