import numpy as np
import matplotlib.pyplot as plt

def decroissanceExp (t, tau, N0):
    return N0*np.exp (-t / tau)

# gamme de concentration
temps = np.linspace (0, 7, 100)

# trace du graphique
N0 = 32
tau = 2
plt.plot (temps, decroissanceExp (temps, tau*np.log(2), N0), color='darkorange', lw=5)

# legende et axes
plt.xlabel ('Temps')
plt.ylabel ("Nombre d'atomes")
plt.ylim (0, N0)
plt.xlim (0, 6.5)

axeN = [N0, N0/2, N0/4, N0/8, N0/16, N0/32]

# parametre de la grille
plt.rcParams["figure.figsize"] = (8, 6)
plt.xticks(np.arange(0, 7, 1))
plt.yticks(axeN)
plt.grid (True, lw=2, ls='--')
plt.savefig('decroissance_radio.png', dpi=300)
plt.show ()