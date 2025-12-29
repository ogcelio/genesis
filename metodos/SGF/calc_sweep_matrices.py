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

    # DECLARANDO MATRIZES A, C, D e S
    A: ndarray = identity(HALF_N)
    C: ndarray = zeros((HALF_N, HALF_N))
    D: ndarray = zeros((HALF_N, HALF_N))
    F: ndarray = zeros(HALF_N)

    for index_reg, reg in enumerate(REGS):
        reg_num = reg - 1
        theta = THETA_DICT[f"{index_reg}"]
        source = SOURCE_DICT[f"{index_reg}"]

        soma_F = 0
        for i in range(N):
            soma_F += W[i] * source[i]
        soma_F *= SIGMA_S0[index_reg] / 2

        for i in range(HALF_N):
            # PREENCHENDO AS MATRIZES, EXCETO PARAMETROS ESPECIFICOS DA DIAGONAL PRINCIPAL
            for j in range(HALF_N):
                soma_C = -theta[i][j] * SIGMA_T[reg_num]
                soma_D = -theta[i][j + HALF_N] * SIGMA_T[reg_num]
                for k in range(N):
                    soma_C += theta[k][j] * W[k]
                    soma_D += theta[k][j + HALF_N] * W[k]
                C[i][j] = soma_C
                D[i][j] = soma_D

            # SOMANDO PARAMETROS ESPECIFICOS DA DIAGONAL PRINCIPAL
            C[i][i] += MI[i] / H[index_reg]
            A[i][i] = MI[i] / H[index_reg]

            F[i] = soma_F - SIGMA_T[i] * source[i] + Q[index_reg]

        inv_a = inv(A)
        GP_DICT.update({f"{index_reg}": inv_a @ C})
        GM_DICT.update({f"{index_reg}": inv_a @ D})
        K_DICT.update({f"{index_reg}": inv_a @ F})

    return GP_DICT, GM_DICT, K_DICT
