from numpy import exp, ndarray, zeros
from numpy.linalg import inv


def calc_theta(
    N: int,
    H: ndarray,
    SIGMA_T: list,
    REGS: list,
    EIGEN_DICT: dict,
) -> dict:
    # CONSTANTES
    HALF_N = N // 2

    # CRIANDO DICIONARIO DOS THETAS DE TODOS OS NODOS
    theta = dict()

    # MONTANDO DICIONARIO DE THETAS
    for index_reg, reg in enumerate(REGS):
        # CRIANDO A MATRIZ DE THETAS
        theta_matrix = zeros((N, N))

        # CRIANDO A MATRIZ A
        A = zeros((N, N))

        # CRIANDO O VETOR N
        E = zeros(N)

        reg_num = reg - 1

        # COLETANDO AUTOVALORES E AUTOVETORES
        eigenvalues = EIGEN_DICT[f"{reg}"]["eigenvalues"]
        eigenvectors = EIGEN_DICT[f"{reg}"]["eigenvectors"]

        # CONSTANTES
        SIGMA_TH = SIGMA_T[reg_num] * H[index_reg]
        INV_SIGMA_TH = 1 / SIGMA_TH

        # MONTANDO A MATRIZ A

        # PRIMEIRAS METADE DAS COLUNAS
        for i in range(N):
            for j in range(HALF_N):
                if eigenvalues[i] > 0:
                    A[i][j] = eigenvectors[j][i]
                else:
                    A[i][j] = eigenvectors[j][i] * exp(SIGMA_TH / eigenvalues[i])

        # SEGUNDA METADE DAS COLUNAS
        for i in range(N):
            for j in range(HALF_N, N):
                if eigenvalues[i] < 0:
                    A[i][j] = eigenvectors[j][i]
                else:
                    A[i][j] = eigenvectors[j][i] * exp((-SIGMA_TH) / eigenvalues[i])

        # MONTANDO OS VETORES THETAS
        for m in range(N):
            # MONTANDO O VETOR E
            for i in range(N):
                if eigenvalues[i] > 0:
                    E[i] = (
                        eigenvalues[i]
                        * eigenvectors[m][i]
                        * (1 - exp((-SIGMA_TH) / eigenvalues[i]))
                    )
                else:
                    E[i] = (
                        eigenvalues[i]
                        * eigenvectors[m][i]
                        * (exp(SIGMA_TH / eigenvalues[i]) - 1)
                    )

            # MONTANDO COLUNA DA MATRIZ THETA:
            theta_vector = (INV_SIGMA_TH * inv(A)) @ E

            for n in range(N):
                theta_matrix[m][n] = theta_vector[n]

        # COLOCANDO THETA CALCULADO NO DICT
        theta.update({f"{index_reg}": theta_matrix})

    return theta
