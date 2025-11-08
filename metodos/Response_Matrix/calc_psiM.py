from numpy import exp, zeros, ndarray


def calc_psiM(
    N: int,
    H: ndarray,
    SIGMA_T: list,
    psiM: ndarray,
    eigenvalues: ndarray,
    eigenvectors: ndarray,
    inv_aux_in: ndarray,
    sol_dif: ndarray,
    reg: int,
    index_reg: int,
    node: int,
    part_sol: ndarray,
):
    M_matrix = zeros((N, N))

    for i in range(N):
        for j in range(N):
            if eigenvalues[j] > 0:
                exponential = 1 - exp(
                    (-SIGMA_T[reg] * H[index_reg]) / abs(eigenvalues[j])
                )
            else:
                exponential = (
                    exp((-SIGMA_T[reg] * H[index_reg]) / abs(eigenvalues[j])) - 1
                )

            M_matrix[i][j] = eigenvalues[j] * eigenvectors[i][j] * exponential

    psim_vec = (M_matrix @ (inv_aux_in @ sol_dif)) + part_sol

    for m in range(N):
        psiM[node][m] = psim_vec[m] / (SIGMA_T[reg] * H[index_reg])

    return psiM
