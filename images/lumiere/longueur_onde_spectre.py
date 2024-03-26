import numpy as np
import matplotlib.pyplot as plt

# Nombre de points et fréquences balayées en Hz
n = 10000
f1, f2 = 200, 0.5

# Définition du temps et du pas de temps
t = np.linspace (0, 2, 10000)
dt = t[1] - t[0]

# Balayage logarithmique en fréquence
f_inst = np.logspace (np.log10(f1), np.log10(f2), n)
# Intégrale de la fréquence pour obtenir la phase
phi = 2 * np.pi * np.cumsum (f_inst) * dt

# Trace le graphique
plt.plot (t, np.sin(phi), color='darkorange', lw=4)
plt.ylim ([-1.2, 1.2])
plt.rcParams["figure.figsize"] = (40, 6)
plt.savefig ('longueur_onde_spectre.png', dpi=300)
plt.show ()