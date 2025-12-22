from numpy import ndarray, float64, zeros, identity


def g_martrix(
    N: int,
    H: list[float64],
    Q: list[float],
    MI: ndarray,
    W: ndarray,
    REGS: list[int],
    SIGMA_T: list[float],
    SIGMA_S0: list[float],
    THETA_DICT: dict,
    SOURCE_DICT: dict,
) -> dict:
    # CONSTANTES
    HALF_N = N // 2

    # DECLARANDO O DICIONARIOS DE G
    gp = dict()  # G PLUS
    gm = dict()  # G MINUS

    # DECLARANDO MATRIZES A, C, D e S
    A: ndarray = identity(HALF_N)
    C: ndarray = zeros((HALF_N, HALF_N))
    D: ndarray = zeros((HALF_N, HALF_N))
    S: ndarray = identity(HALF_N)

    for index_reg, reg in REGS:
        reg_num = reg - 1
        theta = THETA_DICT[f"{index_reg}"]
        source = SOURCE_DICT[f"{index_reg}"]

        soma_S = 0
        for i in range(N):
            soma_S += W[i] * source[i]
        soma_S *= SIGMA_S0[index_reg] / 2

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

            S[i][i] = soma_S - SIGMA_T[i] * source[i] + Q[index_reg]
