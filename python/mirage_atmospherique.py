import numpy as np
import matplotlib.pyplot as plt

# Conversion des degrée en radian et inversement
def enDegree (angle):
    return angle * 180 / np.pi
def enRadian (angle):
    return angle * np.pi / 180

# Formule B1 de https://emtoolbox.nist.gov/Wavelength/Documentation.asp#AppendixA
# T en °C, P en kPa, RH (humidité) en %
def indiceRefraction (p, T, RH = 50):
    return 1 + 7.86 * 10**(-4) * p / (273 + T) - 1.5 * 10**(-11) * RH * (T**2 + 160)

# Pression atmopshérique d'après https://fr.wikipedia.org/wiki/Variation_de_la_pression_atmosph%C3%A9rique_avec_l%27altitude
# altitude en m
def pressionAtmospherique (altitude):
    return 1013.25 * (1 - 0.0065*altitude / 288.15)**(5.255)

# Gradient de température près d'une surface froide (20 °C/m par défaut pour avoir
# une bonne variation)
# altitude en metre
def gradientTemperature (altitude, variation = 0.2):
    return variation * altitude

# Calcule l'indice de refraction en fonction de l'altitude en m
def indiceRefractionAltitude (altitude, gradient):
    p = pressionAtmospherique (altitude)
    T = gradientTemperature (altitude, gradient)
    return indiceRefraction (p, T)

# Distance parcourue dans une couche d'air d'hauteur h
def distanceParcourueCoucheAir (angle, h):
    return h / np.tan (angle)

# Trajectoire d'un rayon lumineux
def rayon (x, z, angle, signe):
    return z + x * signe * np.tan (angle)

def trajetRayonLumineux (x0, z0, zMax, theta, gradient, couches = 200, color = "red"):
    signe = 1
    dz = (zMax - z0) / (couches - 1)
    trajectoireX = []
    trajectoireZ = []
    hauteurs = []
    for k in range (0, 10000):
        # calcul de la hauteur entre les couches
        z1 = z0
        z2 = z1 + signe * dz
        if (z2 < 0):
            break
        # calcul des indices des refractions des couches
        n1 = indiceRefractionAltitude (z1, gradient)
        n2 = indiceRefractionAltitude (z2, gradient)
        # Calcul de l'angle de refraction à partir de l'angle à l'horizontale
        i = np.pi/2 - theta
        if (signe > 0 and i > np.arcsin (n2/n1)): # si le rayon est réfléchi
            r = i # les angles sont égaux
            signe = -1 # on inverse le trajet
            z0 = z1 - dz # on repart à la hauteur précédente
        else:
            r =  np.arcsin ((n1/n2) * np.sin (i)) # loi de Snell-Descartes
            z0 = z2
            hauteurs.append (z0)
        theta = np.pi/2 - r
        # calcul de la trajectoire du rayon
        d = distanceParcourueCoucheAir (theta, np.abs (z2 - z1))
        x = np.linspace (0, d, 20)
        trajectoireX.extend (x + x0)
        trajectoireZ.extend (rayon (x, z1, theta, signe))
        # mise à jour de la position
        x0 += d
    # affichage de la trajectoire totale
    plt.xlim (0, x0)
    plt.plot (trajectoireX, trajectoireZ, color = color, lw = 4)
    # affiche les couches d'air
    if (couches < 50):
        plt.hlines (hauteurs, 0, x0, linestyles='--', colors='grey', lw = 1)

# Initialisation de la position et de l'angle à l'horizontale du rayon
x0 = 0
z0 = 0
zMax = 25
couches = 100
plt.xlabel ("Distance avec l'objet [m]")
plt.ylabel ("Hauteur dans l'atmosphère [m]")
trajetRayonLumineux(x0, z0, zMax, enRadian (2), 2, couches) # le gradient est sévère pour illustrer
plt.ylim (0, 75)
plt.show()

# for t in np.linspace (15, 40, 10):
#     x0 = 0
#     z0 = 0
#     zMax = 100
#     trajetRayonLumineux (x0, z0, zMax, enRadian(t), 2000)
# plt.xlim (0, 400)