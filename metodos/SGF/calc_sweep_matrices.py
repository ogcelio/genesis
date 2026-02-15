from numpy import identity, ndarray, zeros
from numpy.linalg import inv


def calc_sweep_matrices(
    N: int,
    H: ndarray,
    Q: list[float],
    MI: ndarray,
    W: ndarray,
    REGS: list[int],
    SIGMA_T: list[float],
    SIGMA_S0: list[float],
    THETA_DICT: dict,
    SOURCE_DICT: dict,
) -> tuple[dict, dict, dict]:
    # CONSTANTES
    HALF_N = N // 2

    # DECLARANDO O DICIONARIOS DE G
    GP_DICT = dict()  # G PLUS
    GM_DICT = dict()  # G MINUS
    K_DICT = dict()

    for index_reg, reg in enumerate(REGS):
        # DECLARANDO MATRIZES A, C, D e S
        A: ndarray = identity(HALF_N)
        C: ndarray = zeros((HALF_N, HALF_N))
        D: ndarray = zeros((HALF_N, HALF_N))
        F: ndarray = zeros(HALF_N)

        reg_num = reg - 1
        theta = THETA_DICT[f"{index_reg}"]
        source = SOURCE_DICT[f"{index_reg}"]

        soma_F = 0
        for i in range(N):
            soma_F += W[i] * source[i]
        soma_F *= SIGMA_S0[reg_num] * 0.5

        for l in range(HALF_N):
            # PREENCHENDO AS MATRIZES, EXCETO PARAMETROS ESPECIFICOS DA DIAGONAL PRINCIPAL
            for c in range(HALF_N):
                soma_C = 0
                soma_D = 0
                for n in range(N):
                    soma_C += theta[n][c] * W[n]
                    soma_D += theta[n][c + HALF_N] * W[n]
                soma_C *= SIGMA_S0[reg_num] * 0.5
                soma_D *= SIGMA_S0[reg_num] * 0.5

                C[l][c] = soma_C - (theta[l][c] * SIGMA_T[reg_num])
                D[l][c] = soma_D - (theta[l][c + HALF_N] * SIGMA_T[reg_num])

            # SOMANDO PARAMETROS ESPECIFICOS DA DIAGONAL PRINCIPAL
            C[l][l] += MI[l] / H[index_reg]
            A[l][l] = MI[l] / H[index_reg]

            F[l] = soma_F - (SIGMA_T[reg_num] * source[l]) + Q[reg_num]

        inv_a = inv(A)
        GP_DICT.update({f"{index_reg}": inv_a @ C})
        GM_DICT.update({f"{index_reg}": inv_a @ D})
        K_DICT.update({f"{index_reg}": inv_a @ F})

    return GP_DICT, GM_DICT, K_DICT
