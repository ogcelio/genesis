from numpy import zeros, exp
from numpy.linalg import inv


def calc_alfa(
    N,
    hj,
    eigenvalues,
    eigenvectors,
    sigmaT,
    reg,
    k,
    node,
    psiX,
    part_sol,
):
    solution_difference = zeros(N)
    for i in range(N // 2):
        solution_difference[i] = psiX[node][i] - part_sol[i]
        solution_difference[N // 2 + i] = (
            psiX[node + 1][N // 2 + i] - part_sol[N // 2 + i]
        )

    # CÁLCULO DA MATRIZ GERADORA DOS ALFAS
    alfa_matrix = zeros((N, N))

    for i in range(N // 2):
        # PARTE DE CIMA DA MATRIZ
        for j in range(N):
            if eigenvalues[j] > 0:
                exponential = 1
            else:
                exponential = exp((-sigmaT[reg] * hj[k]) / abs(eigenvalues[j]))

            alfa_matrix[i][j] = eigenvectors[i][j] * exponential

        # PARTE DE BAIXO DA MATRIZ
        for i in range(N // 2, N):
            for j in range(N):
                if eigenvalues[j] < 0:
                    exponential = 1
                else:
                    exponential = exp((-sigmaT[reg] * hj[k]) / abs(eigenvalues[j]))

                alfa_matrix[i][j] = eigenvectors[i][j] * exponential

    inv_alfa_matrix = inv(alfa_matrix)

    # CÁLCULO DOS ALFAS
    alfa = inv_alfa_matrix @ solution_difference

    return alfa
