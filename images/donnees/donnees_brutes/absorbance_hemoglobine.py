import numpy as np
import matplotlib.pyplot as plt

# Calcul de l'absorbance à partir du coefficient d'extinction molaire
def absorbance (extinction, concentrationMassique):
    concentrationMolaireRef = 64.5
    return concentrationMassique * np.asarray(extinction) / concentrationMolaireRef
    
# Extraction des données https://omlc.org/spectra/hemoglobin/summary.html
fileName = "molar_extinction_hemoglobine.txt"
file = open (fileName, "r")
lines = file.readlines ()
longueurOnde = []
eHb = []
eHbO = []
count = 0
for line in lines:
    if (count < 2):
        count += 1
        continue
    longueurOnde.append (float (line.split ()[0]))
    eHbO.append (float (line.split ()[1]))
    eHb.append (float (line.split ()[2]))
file.close ()

# Quelques concentration
concentration = np.linspace (40.0, 200.0, 5)
color = ['#E47CB9', '#D6519F', '#C9308A', '#BD0972', '#900356']
count = 0

# Trace les courbes d'absorbance
for c in concentration:
  plt.plot (longueurOnde, absorbance (eHb, c),
            color=color[count], lw=5,
            label = "$c_m = $ {}".format (c) + " g$\cdot$L$^{-1}$")
  count += 1
  
# Paramètres d'affichage
plt.xlim ([250, 650])
plt.ylim ([0, 1.75e6])
plt.xticks (np.arange (250, 650, 50))
plt.yticks (np.arange (0, 1.75e6, 20e4))
plt.legend (prop={'size': 18})
plt.grid (True, lw=2, ls='--')
plt.rcParams["figure.figsize"] = (12, 6)
plt.savefig ('absorbance_hemoglobine_brut.png', dpi=300)
plt.show ()