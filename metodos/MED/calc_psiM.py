from numpy import exp, zeros
from copy import deepcopy


def calc_psiM(
    N, hj, alfa, part_sol, eigenvalues, eigenvectors, sigmaT, node, reg, k, psiM
):
    for i in range(N):
        soma = 0
        for j in range(N):
            if eigenvalues[j] > 0:
                exponencial = 1 - exp((-sigmaT[reg] * hj[k]) / abs(eigenvalues[j]))
            else:
                exponencial = exp((-sigmaT[reg] * hj[k]) / abs(eigenvalues[j])) - 1

            soma += eigenvalues[j] * alfa[j] * eigenvectors[i][j] * exponencial
        psiM[node][i] = ((1 / (hj[k] * sigmaT[reg])) * soma) + part_sol[i]

    return psiM
