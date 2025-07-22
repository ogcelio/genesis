from numpy import zeros


def calc_ssj(N, NN, NNT, regioes, psiM, w, sigmaS0):
    regiao = regioes[0] - 1
    nodo = 0
    Ssj = zeros(NNT)
    i = 0
    for j in range(NNT):
        soma = 0
        if nodo == NN[i]:
            i += 1
            regiao = regioes[i] - 1
            nodo = 0

        for m in range(N):
            soma += w[m] * psiM[j][m]
        Ssj[j] = (sigmaS0[regiao] / 2) * soma
        nodo += 1

    return Ssj
