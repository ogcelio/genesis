from copy import deepcopy


def foward(N, NN, NNT, regs, psiX, hj, Ssj, Qj, mi, sigmaT, sigmaS0):
    reg = regs[0] - 1
    node = 0
    i = 0
    psiX_foward = deepcopy(psiX)
    for j in range(1, NNT + 1):
        if node == NN[i]:
            i += 1
            reg = regs[i] - 1
            node = 0
        for m in range(N // 2):
            psiX_foward[j][m] = (
                (((mi[m] / hj[i]) - (sigmaT[reg] / 2)) * psiX_foward[j - 1][m])
                + Ssj[j - 1]
                + Qj[reg]
            ) / ((mi[m] / hj[i]) + (sigmaT[reg] / 2))
        node += 1

    return psiX_foward
