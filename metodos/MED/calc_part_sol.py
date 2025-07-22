from numpy.linalg import inv
from numpy import zeros


def calc_part_sol(N, Qj, reg, sigmaT, sigmaS0, w):
    p_matrix = zeros((N, N))
    for i in range(N):
        for j in range(N):
            if i == j:
                p_matrix[i][j] = sigmaT[reg] - ((sigmaS0[reg] * w[j]) / 2)

            else:
                p_matrix[i][j] = -((sigmaS0[reg] * w[j]) / 2)
    inv_p_matrix = inv(p_matrix)

    source = [Qj[reg] for _ in range(N)]
    part_sol = inv_p_matrix @ source

    return part_sol
