from numpy import zeros, ndarray


def foward(N: int, GP: ndarray, GM: ndarray, K: ndarray, psi: ndarray, node: int):
    # CONSTANTES
    HALF_N = N // 2

    # VETOR DE FLUXOS DE ENTRADA A ESQUERDA
    psi_left = zeros(HALF_N)

    # VETOR DE FLUXOS DE ENTRADA A DIREITA
    psi_right = zeros(HALF_N)

    # PREENCHENDO VETORES
    for i in range(HALF_N):
        psi_left[i] = psi[node - 1][i]
        psi_right[i] = psi[node][i + HALF_N]

    # VETOR DE IDA
    psi_foward = (GP @ psi_left) + (GM @ psi_right) + K

    for i in range(HALF_N):
        psi[node][i] = psi_foward[i]


def backward(N, GP, GM, K, psi, node):
    # CONSTANTES
    HALF_N = N // 2

    # VETOR DE FLUXOS DE ENTRADA A ESQUERDA
    psi_left = zeros(HALF_N)

    # VETOR DE FLUXOS DE ENTRADA A DIREITA
    psi_right = zeros(HALF_N)

    # PREENCHENDO VETORES
    for i in range(HALF_N):
        psi_left[i] = psi[node][i]
        psi_right[i] = psi[node + 1][i + HALF_N]

    # VETOR DE IDA
    psi_backward = (GP @ psi_right) + (GM @ psi_left) + K

    for i in range(HALF_N):
        psi[node][i + HALF_N] = psi_backward[i]
