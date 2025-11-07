from numpy.linalg import inv
from numpy import zeros, ndarray


def calc_part_sol(N: int, Q: list, SIGMA_T: list, SIGMA_S0: list, W: ndarray, reg: int):
    p_matrix = zeros((N, N))
    for i in range(N):
        for j in range(N):
            if i == j:
                p_matrix[i][j] = SIGMA_T[reg] - ((SIGMA_S0[reg] * W[j]) / 2)

            else:
                p_matrix[i][j] = -((SIGMA_S0[reg] * W[j]) / 2)
    inv_p_matrix = inv(p_matrix)

    source = [Q[reg] for _ in range(N)]
    part_sol = inv_p_matrix @ source

    return part_sol
