from numpy import exp


def calc_psiX(
    N, hj, alfa, part_sol, eigenvalues, eigenvectors, sigmaT, node, reg, k, psiX
):
    for i in range(N // 2):
        soma = 0
        for j in range(N):
            if eigenvalues[j] < 0:
                exponencial = 1
            else:
                exponencial = exp((-sigmaT[reg] * hj[k]) / abs(eigenvalues[j]))

            soma += alfa[j] * eigenvectors[i][j] * exponencial

        psiX[node + 1][i] = soma + part_sol[i]

    for i in range(N // 2, N):
        soma = 0
        for j in range(N):
            if eigenvalues[j] > 0:
                exponencial = 1
            else:
                exponencial = exp((-sigmaT[reg] * hj[k]) / abs(eigenvalues[j]))
            soma += alfa[j] * eigenvectors[i][j] * exponencial

        psiX[node][i] = soma + part_sol[i]

    return psiX
