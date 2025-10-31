from numpy import zeros, exp


def calc_aux_em(
    N,
    hj,
    eigenvalues,
    eigenvectors,
    sigmaT,
    reg,
    k,
):
    # CÁLCULO DA MATRIZ AUXILIAR DOS INCIDENTES
    aux_em = zeros((N, N))

    for i in range(N // 2):
        # PARTE DE CIMA DA MATRIZ
        for j in range(N):
            if eigenvalues[j] < 0:
                exponential = 1
            else:
                exponential = exp((-sigmaT[reg] * hj[k]) / abs(eigenvalues[j]))

            aux_em[i][j] = eigenvectors[i][j] * exponential

        # PARTE DE BAIXO DA MATRIZ
        for i in range(N // 2, N):
            for j in range(N):
                if eigenvalues[j] > 0:
                    exponential = 1
                else:
                    exponential = exp((-sigmaT[reg] * hj[k]) / abs(eigenvalues[j]))

                aux_em[i][j] = eigenvectors[i][j] * exponential

    return aux_em
