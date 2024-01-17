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

def Wien (temperature):
    return 2.9e-3 / temperature


def traceCorpsChaud ():
    # longueur d'onde
    lambd = np.linspace (0.1, 4, 200)
    plt.xlim ((0, 4))
    
    plt.plot (lambd, luminance (lambd, 1000), lw=5, label="                          ")
    plt.plot (lambd, luminance (lambd, 3000), lw=5, label=" ")
    plt.plot (lambd, luminance (lambd, 4000), lw=5, label=" ")
    plt.plot (lambd, luminance (lambd, 5000), lw=5, label=" ")
    plt.legend()

    plt.xlabel("$\lambda$ ($\mu$m)")
    plt.ylabel("Flux lumineux")
    
    plt.rcParams["figure.figsize"] = (6, 6)
    plt.savefig ('luminance_corps_chaud.png', dpi=300, transparent=True)
    plt.show ()
    
    
def traceCorpsChaudT3000 ():
    lambd = np.linspace (0.1, 4, 200)
    plt.xlim ((0, 4))
    plt.plot (lambd, luminance (lambd, 4000), lw=5)

    plt.xlabel("$\lambda$ ($\mu$m)")
    plt.ylabel("Flux lumineux")
    
    plt.rcParams["figure.figsize"] = (6, 6)
    plt.savefig ('luminance_corps_chaud_T3000.png', dpi=300, transparent=True)
    plt.show ()
    
    
def traceWien ():
    T = np.linspace (300, 5000, 200)
    plt.plot (T, Wien (T), lw=5)

    plt.xlabel("$T$ (K))")
    plt.ylabel("$\lambda$ (m)")

    plt.rcParams["figure.figsize"] = (6, 6)
    plt.savefig ('loi_wien.png', dpi=300, transparent=True)
    plt.show ()
    
def traceChauffage ():
    lambd = np.linspace (0.1, 20, 200)
    plt.xlim ((0, 20))
    temperature = np.linspace (300, 700, 10)
    for T in temperature:
        plt.plot (lambd, luminance (lambd, T), lw=5)

    plt.xlabel ("$\lambda$ ($\mu$m)")
    plt.ylabel ("Flux lumineux")
    plt.plot ()
    
    
# traceCorpsChaud()
# traceCorpsChaudT3000()
# traceWien()
traceChauffage ()