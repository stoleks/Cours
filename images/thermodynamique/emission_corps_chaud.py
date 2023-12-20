import numpy as np
import matplotlib.pyplot as plt


# Quelque constantes
h = 6.62607015e-34
kB = 1.380649e-23
c = 2.997924e8

# Loi d'émission des corps chaud
def luminance (longueurOnde, temperature):
    lambd = longueurOnde * 10**(-6)
    E = h * c / (kB * lambd * temperature)
    norm = 2*h*c*c / (lambd**5)
    return norm / (np.exp (E) - 1)


# longueur d'onde
lambd = np.linspace (0.1, 4, 200)

# trace du graphique
plt.xlim ((0, 4))
plt.plot (lambd, luminance (lambd, 1000), lw=5, label="                          ")
plt.plot (lambd, luminance (lambd, 3000), lw=5, label=" ")
plt.plot (lambd, luminance (lambd, 4000), lw=5, label=" ")
plt.plot (lambd, luminance (lambd, 5000), lw=5, label=" ")

plt.xlabel("$\lambda$ ($\mu$m)")
plt.ylabel("Flux lumineux")
plt.legend()

# parametre de la grille
plt.rcParams["figure.figsize"] = (6, 6)
plt.savefig ('luminance_corps_chaud.png', dpi=300, transparent=True)
plt.show ()