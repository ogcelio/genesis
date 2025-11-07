from numpy import exp, ndarray


def calc_psi(
    N: int,
    H: ndarray,
    SIGMA_T: list,
    alfa: ndarray,
    part_sol: ndarray,
    eigenvalues: ndarray,
    eigenvectors: ndarray,
    node: int,
    reg: int,
    index_reg: int,
    psi: ndarray,
):
    for i in range(N // 2):
        soma = 0
        for j in range(N):
            if eigenvalues[j] < 0:
                exponencial = 1
            else:
                exponencial = exp((-SIGMA_T[reg] * H[index_reg]) / abs(eigenvalues[j]))

            soma += alfa[j] * eigenvectors[i][j] * exponencial

        psi[node + 1][i] = soma + part_sol[i]

    for i in range(N // 2, N):
        soma = 0
        for j in range(N):
            if eigenvalues[j] > 0:
                exponencial = 1
            else:
                exponencial = exp((-SIGMA_T[reg] * H[index_reg]) / abs(eigenvalues[j]))
            soma += alfa[j] * eigenvectors[i][j] * exponencial

        psi[node][i] = soma + part_sol[i]

    return psi
