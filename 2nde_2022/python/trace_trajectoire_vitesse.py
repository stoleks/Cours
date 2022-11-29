import numpy as np # bibliotheque de calcul
import matplotlib.pyplot as plt # blibliotheque d'affichage

# dessine une fleche partant du point 'depart' et allant au point 'fin'
def traceFleche (depart, fin) :
    taille = 0.025 # taille de la pointe de la fleche
    plt.arrow (depart[0], depart[1], fin[0], fin[1], # coordonnees du vecteur
               head_length=taille, head_width=taille) # apparence du vecteur

# calcul et trace le vecteur vitesse
def traceVecteurVitesses (x, y, Dt) :
    for i in range (1, len (x) - 1) :
        vx = (x[i + 1] - x[i - 1]) / (2*Dt)
        vy = (y[i + 1] - y[i - 1]) / (2*Dt)
        traceFleche ((x[i], y[i]), (vx, vy))

# reglage du graphique
plt.axis('equal') # pour avoir des vecteurs symetriques
plt.xlabel (r'$x$ (en cm)') # legende de l'abscisse
plt.ylabel (r'$y$ (en cm)') # legende de l'ordonnee
plt.title ("Trajectoire d'une goutte d'encre") # titre du graphique

# definition de la trajectoire
Dt = 5
x = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
y = [0.02, 0.04, 0.16, 0.32, 0.64, 1.28, 1.96, 2.56, 3.20, 3.84, 3.84, 3.84, 3.84, 0, 0, 0, 0, 0]

# trace les positions et les vecteurs vitesses
plt.plot (x, y, 'gx') # g : vert (green), o : cercle
traceVecteurVitesses (x, y, Dt) # trace les vitesses
plt.show () # affiche le graphique
