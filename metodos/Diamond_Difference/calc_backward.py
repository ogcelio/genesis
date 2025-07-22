from copy import deepcopy


def backward(N, NN, NNT, regs, psiX, hj, Ssj, Qj, mi, sigmaT, sigmaS0):
    ultima_regiao = len(regs) - 1
    regiao = regs[ultima_regiao] - 1
    nodo = 0
    i = ultima_regiao
    psiX_backward = deepcopy(psiX)
    for j in range(NNT - 1, -1, -1):
        if nodo == NN[i]:
            i -= 1
            regiao = regs[i] - 1
            nodo = 0
        for m in range((N // 2), N):
            psiX_backward[j][m] = (
                (
                    ((abs(mi[m]) / hj[i]) - (sigmaT[regiao] / 2))
                    * psiX_backward[j + 1][m]
                )
                + Ssj[j]
                + Qj[regiao]
            ) / ((abs(mi[m]) / hj[i]) + (sigmaT[regiao] / 2))
        nodo += 1

    return psiX_backward
