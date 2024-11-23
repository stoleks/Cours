import numpy as np
import matplotlib.pyplot as plt

def masseVolumiqueSirop (x):
    return (9 * x + 1000)/1000

# gamme de concentration
concentration = np.linspace (0, 30, 100)

# trace du graphique
plt.xlim ((0, 25))
plt.ylim ((1.000, 1.220))
plt.plot (concentration, masseVolumiqueSirop (concentration), color='darkorange', lw=5)

# legende
plt.xlabel ('Masse de sucre (g)')
plt.ylabel ('Masse volumique (g/mL)')

# parametre de la grille
plt.rcParams["figure.figsize"] = (6, 6)
plt.xticks(np.arange(0, 28, 5))
plt.yticks(np.arange(1.000, 1.240, 0.040))
plt.grid (True, lw=2, ls='--')
plt.savefig('masse_volumique_sirop.png', dpi=300)
plt.show ()