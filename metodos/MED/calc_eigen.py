from numpy.linalg import eig
from numpy import zeros


def calc_eigen(N, reg, mi, w, C0j):
    A_matrix = zeros((N, N))

    ###ETAPA CÁLCULO DA MATRIZ DE AUTOVALORES E AUTOVETORES
    for i in range(N):
        for j in range(N):
            if i == j:
                A_matrix[i][j] = (1 / mi[i]) - ((C0j[reg] * w[j]) / (2 * mi[i]))

            else:
                A_matrix[i][j] = -((C0j[reg] * w[j]) / (2 * mi[i]))

    # ENCONTRANDO AUTOVALORES E AUTOVETORES
    eigenvalue_lambda, eigenvectors = eig(A_matrix)
    eigenvalues = eigenvalue_lambda

    # TRANSFORMANDO LAMBDA EM NI
    for i, eigenvalue in enumerate(eigenvalues):
        eigenvalues[i] = 1 / eigenvalue

    return eigenvalues, eigenvectors
