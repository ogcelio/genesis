from numpy import zeros, exp, ndarray


def calc_aux_em(
    N: int,
    H: ndarray,
    SIGMA_T: list,
    eigenvalues: ndarray,
    eigenvectors: ndarray,
    reg: int,
    index_reg: int,
):
    # CÁLCULO DA MATRIZ AUXILIAR DOS INCIDENTES
    aux_em = zeros((N, N))

    for i in range(N // 2):
        # PARTE DE CIMA DA MATRIZ
        for j in range(N):
            if eigenvalues[j] < 0:
                exponential = 1
            else:
                exponential = exp((-SIGMA_T[reg] * H[index_reg]) / abs(eigenvalues[j]))

            aux_em[i][j] = eigenvectors[i][j] * exponential

        # PARTE DE BAIXO DA MATRIZ
        for i in range(N // 2, N):
            for j in range(N):
                if eigenvalues[j] > 0:
                    exponential = 1
                else:
                    exponential = exp(
                        (-SIGMA_T[reg] * H[index_reg]) / abs(eigenvalues[j])
                    )

                aux_em[i][j] = eigenvectors[i][j] * exponential

    return aux_em
