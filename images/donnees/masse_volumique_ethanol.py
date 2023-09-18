import numpy as np
import matplotlib.pyplot as plt

# donnees
proportionVolume = np.array ([
    0.0,   3.13, 5.00,  6.00,  6.30,  8.47,  12.40, 14.0,  15.0,
    18.50, 20.2, 21.5,  22.10, 23.1,  24.50, 24.8,  27.00, 29.5,
    30.40, 32.4, 33.90, 36.1,  36.20, 40.5,  41.90, 46.3,  47.40,
    53.00, 53.8, 58.0,  63.0,  63.6,  68.0,  78.3,  94.00, 100.0
])

masseVolumique = np.array ([
    0.99823, 0.99363, 0.99103, 0.98971, 0.98930, 0.98658, 0.98187, 0.98006, 0.97910,
    0.97511, 0.97336, 0.97194, 0.97129, 0.97024, 0.96863, 0.96823, 0.96578, 0.96283,
    0.96168, 0.95914, 0.95710, 0.95400, 0.95382, 0.94715, 0.94486, 0.93720, 0.93510,
    0.92406, 0.92193, 0.91349, 0.90220, 0.90008, 0.89038, 0.86311, 0.81529, 0.78934
])

# trace du graphique
plt.plot (proportionVolume / 100, masseVolumique, color='darkorange', lw=5)
plt.xlim (0, 1)
plt.ylim (0.78, 1)
plt.xlabel ("Fraction volumique d'éthanol")
plt.ylabel ("Masse volumique (g/mL)")

# parametre de la grille
plt.rcParams["figure.figsize"] = (6, 6)
plt.xticks(np.arange(0.0, 1.01, 0.2))
plt.yticks(np.arange(0.78, 1.0, 0.04))
plt.grid (True, lw=2, ls='--')

#
plt.savefig('masse_volumique_ethanol.png', dpi=300)
plt.show ()