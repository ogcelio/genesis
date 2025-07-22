from numpy import zeros


def calc_psiM(N, NNT, psiX):
    psiM = zeros((NNT, N))
    for j in range(NNT):
        for m in range(N):
            psiM[j][m] = (1 / 2) * (psiX[j + 1][m] + psiX[j][m])

    return psiM
