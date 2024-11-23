import numpy as np
import matplotlib.pyplot as plt


# Quelque conductivite molaire µS/cm.L/mol
lAg = 6.19e4
lCl = 7.63e4
lNO3 = 7.14e4
lNa = 5.01e4
# Calcul de la conductivite avec Kohlrausch
def conductivite (volume, cAg, nIni):
    nVerse = volume * cAg
    nAg = max (nVerse - nIni, 0)
    nCl = max (nIni - nVerse, 0)
    vTot = (200 + volume) / 1000 # mL -> L
    return (lAg*nAg + lCl*nCl + lNO3*nVerse) / vTot


# concentration molaire et quantite de matiere
cAg = 1e-5 # mol/mL
nCl = 16.5e-5 # mol
# volume verse
volume = np.linspace (0, 22, 100)
conduc = []
for v in volume:
    conduc.append (conductivite (v, cAg, nCl))

# trace du graphique
plt.xlim ((0, np.max (volume)))
plt.plot (volume, conduc, color='darkorange', lw=5)

# parametre de la grille
plt.rcParams["figure.figsize"] = (6, 6)
plt.xticks (np.arange(0, 22, 2))
plt.grid (True, lw=2, ls='--')
plt.savefig ('conductivite_eau.png', dpi=300)
plt.show ()