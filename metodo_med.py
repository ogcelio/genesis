import os
import sys

import numpy as np
from decimal import Decimal, getcontext

path_quadratura = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(path_quadratura)

from quadratura.quadratura_backend import quadratura

# propriedades_1grupo = [
#     ["1", "0.9500", "0", "0", "0", "0"],
#     ["1", "0.9300", "0", "0", "0", "0"],
#     ["1", "0.9800", "0", "0", "0", "0"],
#     ["1", "0.9200", "0", "0", "0", "0"],
#     ["1", "0.9100", "0", "0", "0", "0"],
#     ["1", "0.8500", "0", "0", "0", "0"],
#     ["0.2500", "0.0500", "0", "0", "0", "0.2200"],
#     ["0.3333", "0.2333", "0", "0", "0", "0.3243"],
#     ["0.2777", "0.1777", "0", "0", "0", "0.2042"],
#     ["0.3333", "0.2333", "0", "0", "0", "0"],
# ]
sigmaT = [1, 1, 1, 1, 1, 1, 0.2500, 0.3333, 0.2777, 0.3333]
sigmaS0 = [
    0.9500,
    0.9300,
    0.9800,
    0.9200,
    0.9100,
    0.8500,
    0.0500,
    0.2333,
    0.1777,
    0.2333,
]
getcontext().prec = 50
sigmaT = [Decimal(sigma) for sigma in sigmaT]
sigmaS0 = [Decimal(sigma) for sigma in sigmaS0]


def med(N, sigmaS0, sigmaT):
    C0j = []
    for i in range(len(sigmaT)):
        C0j.append(sigmaS0[i] / sigmaT[i])
    mi, w = quadratura(N)

    A_chapeu = [[0 for m in range(N)] for m in range(N)]
    for i in range(N):
        for j in range(N):
            if i == j:
                A_chapeu[i][j] = float((1 / mi[i]) - ((C0j[i] * w[j]) / (2 * mi[i])))
            else:
                A_chapeu[i][j] = float(-((C0j[i] * w[j]) / (2 * mi[i])))
    print(A_chapeu)
    autovalores, autovetores = np.linalg.eig(A_chapeu)
    autovetores = np.transpose(autovetores)
    return autovalores, autovetores


N = 4
# A = np.array(med(N, sigmaS0, sigmaT))
ni, am = med(N, sigmaS0, sigmaT)
print(ni, am)
# autovalores, autovetores = np.linalg.eig(A)
# print("Autovalores:", autovalores)
# print("Autovetores:", autovetores)
# autovetores = np.transpose(autovetores)
# print("Autovetores:", autovetores)
# for i in range(len(autovetores)):
#     autovetores[i] = autovetores[i] / abs(min(autovetores[i]))
# print("Autovetores:", autovetores)  # normalizado
# # print(autovetores[0] / abs(min(autovetores[0])))
