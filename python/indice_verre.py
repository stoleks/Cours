import numpy as np
import matplotlib.pyplot as plt

def carre (nombre):
    return (nombre * nombre)

# Objet qui calcul l'indice optique d'un verre
class IndiceVerre:
    # nD = indice pour la raie D, VD = nombre d'Abbe pour la raie D
    # les raies sont en nanometre 
    def __init__(self, nD, VD):
        raieC = carre (656.3)
        raieD = carre (589.3)
        raieF = carre (486.1)
        # formule 
        self.B = (nD - 1) / (VD*(1 / raieF- 1 / raieC))
        self.A = nD - self.B / raieD
    
    # formule de cauchy
    def indice (self, Lambda):
        n = self.A + self.B / carre (Lambda)
        return n
    
    # calcul un tableau entier
    def indices (self, Lambda):
        n = []
        for k in range (len (Lambda)):
            n.append (self.indice (Lambda[k]))
        return n

# gamme de longueur d'onde
Lambda = np.linspace (350, 800, 1000)

# definition de quelques verre
crown = IndiceVerre (1.51, 60)
crownFlint = IndiceVerre (1.53, 52)
flintDense = IndiceVerre (1.60, 38)

fig, graph = plt.subplots(figsize = (31, 18))
# trace de l'indice de quelque verre
#plt.plot (Lambda, crownFlint.indices (Lambda), color='g', label='Crown Flint')
#plt.plot(Lambda, crown.indices (Lambda), color='r', label='Crown')
plt.ylim ((1.58, 1.66))
graph.plot (Lambda, flintDense.indices (Lambda), color='darkorange', lw=16, label='Flint Dense')

# parametre du graphique
plt.xlabel ('lambda (nm)')
plt.ylabel ('n')
# plt.legend ()
plt.grid (True, lw=4, ls='--')
plt.show ()