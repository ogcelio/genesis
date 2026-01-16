from numpy import ndarray, zeros


def foward(N: int, GP: ndarray, GM: ndarray, K: ndarray, psi: ndarray, node: int):
    # CONSTANTES
    HALF_N = N // 2

    # VETOR DE FLUXOS DE ENTRADA A ESQUERDA
    psi_left = zeros(HALF_N)

    # VETOR DE FLUXOS DE ENTRADA A DIREITA
    psi_right = zeros(HALF_N)

    # PREENCHENDO VETORES
    for m in range(HALF_N):
        psi_left[m] = psi[node - 1][m]
        psi_right[m] = psi[node][m + HALF_N]

    # VETOR DE IDA
    psi_foward = (GP @ psi_left) + (GM @ psi_right) + K

    for m in range(HALF_N):
        psi[node][m] = psi_foward[m]


def backward(N, GP, GM, K, psi, node):
    # CONSTANTES
    HALF_N = N // 2

    # VETOR DE FLUXOS DE ENTRADA A ESQUERDA
    psi_left = zeros(HALF_N)

    # VETOR DE FLUXOS DE ENTRADA A DIREITA
    psi_right = zeros(HALF_N)

    # PREENCHENDO VETORES
    for m in range(HALF_N):
        psi_left[m] = psi[node][m]
        psi_right[m] = psi[node + 1][m + HALF_N]

    # VETOR DE IDA
    psi_backward = (GP @ psi_right) + (GM @ psi_left) + K

    for m in range(HALF_N):
        psi[node][m + HALF_N] = psi_backward[m]
