from numpy import zeros


def calc_sol_dif(N, psiX, node, part_sol):
    solution_difference = zeros(N)
    for i in range(N // 2):
        solution_difference[i] = psiX[node][i] - part_sol[i]
        solution_difference[N // 2 + i] = (
            psiX[node + 1][N // 2 + i] - part_sol[N // 2 + i]
        )

    return solution_difference
