from numpy import ndarray, exp, zeros
from numpy.linalg import inv


def calc_theta(
    N: int,
    H: ndarray,
    SIGMA_T: list,
    REGS: list,
    EIGEN_DICT: dict,
) -> dict:
    # CRIANDO A MATRIZ DE THETAS
    theta_matrix = zeros((N, N))

    # CRIANDO DICIONARIO DOS THETAS DE TODOS OS NODOS
    theta = dict()

    # CRIANDO A MATRIZ A
    A = zeros((N, N))

    # CRIANDO O VETOR N
    E = zeros(N)

    # MONTANDO DICIONARIO DE THETAS
    for index_reg, reg in enumerate(REGS):
        reg_num = reg - 1

        # COLETANDO AUTOVALORES E AUTOVETORES
        eigenvalues = EIGEN_DICT[f"{index_reg}"]["eigenvalues"]
        eigenvectors = EIGEN_DICT[f"{index_reg}"]["eigenvectors"]

        # CONSTANTES
        SIGMA_TH = SIGMA_T[reg_num] * H[index_reg]
        INV_SIGMA_TH = 1 / SIGMA_TH

        # MONTANDO OS VETORES THETAS
        for m in range(N):
            # MONTANDO A MATRIZ A
            for i in range(N // 2):
                for j in range(N // 2):
                    # PRIMEIRO QUADRANTE
                    A[i][j] = eigenvectors[j][i]

                    # SEGUNDO QUADRANTE
                    A[i][j + N // 2] = eigenvectors[j + N // 2][i] * exp(
                        (-SIGMA_TH) / eigenvalues[j]
                    )

                    # TERCEIRO QUADRANTE
                    A[i + N // 2][j] = eigenvectors[j][i + N // 2] * exp(
                        SIGMA_TH / eigenvalues[j + N // 2]
                    )

                    # QUARTO QUADRANTE
                    A[i + N // 2][j + N // 2] = eigenvectors[j + N // 2][i + N // 2]

            # MONTANDO O VETOR E
            for i in range(N // 2):
                # PRIMEIRA METADE
                E[i] = (
                    eigenvalues[i]
                    * eigenvectors[m][i]
                    * (1 - exp((-SIGMA_TH) / eigenvalues[i]))
                )

                # SEGUNDA METADE
                E[i + N // 2] = (
                    eigenvalues[i + N // 2]
                    * eigenvectors[m][i + N // 2]
                    * (exp(SIGMA_TH / eigenvalues[i + N // 2]))
                )

            # MONTANDO LINHA DA MATRIZ THETA:
            theta_vector = INV_SIGMA_TH * (inv(A) @ E)

            for n in range(N):
                theta_matrix[m][n] = theta_vector[n]

        # COLOCANDO THETA CALCULADO NO DICT
        theta.update({f"{index_reg}": theta_matrix})

    return theta
