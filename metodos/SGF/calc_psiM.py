from numpy import ndarray


def calc_psiM(
    N: int,
    REGS: list | tuple,
    NUM_NODES: list | tuple,
    THETA_DICT: dict,
    SOURCE_DICT: dict,
    PSI: ndarray,
    psim: ndarray,
):
    HALF_N = N // 2
    node = 0
    for index_reg, num_nodes in enumerate(NUM_NODES):
        theta = THETA_DICT[f"{index_reg}"]
        source = SOURCE_DICT[f"{index_reg}"]

        for j in range(num_nodes):
            for m in range(N):
                soma = source[m]
                for n in range(HALF_N):
                    soma += theta[m][n] * PSI[node][n]

                    soma += theta[m][n + HALF_N] * PSI[node + 1][n + HALF_N]

                psim[node][m] = soma
            node += 1
