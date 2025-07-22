def calc_psiX(
    N,
    psiX,
    psiM,
    Ssj,
    hj,
    Qj,
    sigmaT,
    mi,
    node,
    reg,
    k,
):
    for m in range(N // 2):
        psiX[node + 1][m] = (
            (hj[k] / abs(mi[m])) * (Ssj[node] + Qj[reg] - (sigmaT[reg] * psiM[node][m]))
        ) + psiX[node][m]

    for m in range(N // 2, N):
        psiX[node][m] = (
            (hj[k] / abs(mi[m])) * (Ssj[node] + Qj[reg] - (sigmaT[reg] * psiM[node][m]))
        ) + psiX[node + 1][m]

    return psiX
