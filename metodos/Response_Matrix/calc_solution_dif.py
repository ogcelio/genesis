from numpy import zeros, ndarray


def calc_sol_dif(N: int, psi: ndarray, node: int, part_sol: ndarray):
    solution_difference = zeros(N)
    for i in range(N // 2):
        solution_difference[i] = psi[node][i] - part_sol[i]
        solution_difference[N // 2 + i] = (
            psi[node + 1][N // 2 + i] - part_sol[N // 2 + i]
        )

    return solution_difference
