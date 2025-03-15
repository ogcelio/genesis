import os
import sys

import numpy as np
from decimal import Decimal, getcontext

path_quadratura = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(path_quadratura)

from quadratura.quadratura_backend import quadratura


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


def med(
    sigmaT,
    sigmaS0,
    sigmaS1,
    sigmaS2,
    Qj,
    NiSigmaF,
    N,
    cce,
    ccd,
    precisao,
    NN,
    regioes,
    n_regioes,
    esp_R,
):
    matrizes_A = []
    matrizes_B = []
    solucoes = []
    NNT = int(sum(NN))
    pt = NNT + 1
    C0j = []
    for i in range(len(sigmaT)):
        C0j.append(sigmaS0[i] / sigmaT[i])
    mi, w = quadratura(N)

    regiao = regioes[0] - 1
    nodo = 0
    k = 0
    for nodo_nodo in range(NNT):
        A_chapeu = [[0 for m in range(N)] for m in range(N)]
        for i in range(N):
            for j in range(N):
                if i == j:
                    A_chapeu[i][j] = (1 / mi[i]) - ((C0j[regiao] * w[j]) / (2 * mi[i]))
                else:
                    A_chapeu[i][j] = -((C0j[regiao] * w[j]) / (2 * mi[i]))

        for i in range(N):
            for j in range(N):
                A_chapeu[i][j] = float(A_chapeu[i][j])

        matrizes_A.append(A_chapeu)
        autovalores, autovetores = np.linalg.eig(A_chapeu)
        autovetores = np.transpose(autovetores)

        B_chapeu = [[0 for m in range(N)] for m in range(N)]
        for i in range(N):
            for j in range(N):
                if i == j:
                    B_chapeu[i][j] = sigmaT[regiao] - ((sigmaS0[regiao] * w[j]) / 2)
                else:
                    B_chapeu[i][j] = -(sigmaS0[regiao] * w[j]) / 2

        for i in range(N):
            for j in range(N):
                B_chapeu[i][j] = float(B_chapeu[i][j])

        matrizes_B.append(B_chapeu)
        B_chapeu_inversa = np.linalg.inv(B_chapeu)

        fonte = [Qj[regiao] for _ in range(N)]
        solucao_particular = B_chapeu_inversa @ fonte
        solucoes.append(solucao_particular.tolist())

        if nodo == NN[k]:
            k += 1
            regiao = regioes[k] - 1
            nodo = 0
        nodo += 1

    return autovalores, autovetores, solucoes


N = 4
n_regioes = 1
sigmaT = [Decimal(f"{sigma}") for sigma in sigmaT]
sigmaS0 = [Decimal(f"{sigma}") for sigma in sigmaS0]
Qj = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
NN = [1]
ni, am, solucoes = med(
    sigmaT,
    sigmaS0,
    [],
    [],
    Qj,
    [],
    N,
    1,
    0,
    10e-6,
    NN,
    [1],
    n_regioes,
    [5],
)

print(ni, "\n\n", am, "\n\n", solucoes)
