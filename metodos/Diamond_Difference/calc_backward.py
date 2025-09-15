from copy import deepcopy


def backward(N, NN, NNT, regs, psiX, hj, Ssj, Qj, mi, sigmaT):
    """
    Calcula os fluxos angulares do processo iterativo de volta do método numérico Diamond Difference.

    Parâmetros:
    ----------
    N -> int
        Ordem da quadratura do problema.
    NN -> Array (Lista, Tupla ou Array NumPy)
        Contém o número de nodos de cada REGIÃO do domínio.
    NNT -> int
        Quantidade de nodos totais do domínio.
    regs -> Array (Lista, Tupla ou Array Numpy)
        Contém a zona material de cada REGIÃO do domínio.
    psiX -> Array Numpy
        Contém todos os N fluxos angulares do domínio, separados por cada PONTO do mesmo.
    hj -> Array (Lista, Tupla ou Array Numpy)
        Contém o tamanho dos nodos de cada REGIÃO do domínio.
    Ssj -> Array (Lista, Tupla ou Array Numpy)
        Contém o valor da fonte de espalhamento de cada NODO do domínio.
    Qj -> Array (Lista, Tupla ou Array Numpy)
        Contém o valor da fonte fixa em cada REGIÃO do domínio.
    mi -> Array (Lista, Tupla ou Array Numpy)
        Contém o valor das N raízes do polinônio de Lagrange, que representam as direções discretas de propagação das particulas neutras.
    sigmaT -> Array (Lista, Tupla ou Array Numpy)
        Contém o valor da seção de choque macroscópica total de cada REGIÃO.

    Retorna:
    -------
    psiX -> Array Numpy
        Fluxos angulares atualizados.
    """
    ultima_regiao = len(regs) - 1
    regiao = regs[ultima_regiao] - 1
    nodo = 0
    i = ultima_regiao
    psiX_backward = deepcopy(psiX)
    for j in range(NNT - 1, -1, -1):
        if nodo == NN[i]:
            i -= 1
            regiao = regs[i] - 1
            nodo = 0
        for m in range((N // 2), N):
            psiX_backward[j][m] = (
                (
                    ((abs(mi[m]) / hj[i]) - (sigmaT[regiao] / 2))
                    * psiX_backward[j + 1][m]
                )
                + Ssj[j]
                + Qj[regiao]
            ) / ((abs(mi[m]) / hj[i]) + (sigmaT[regiao] / 2))
        nodo += 1

    return psiX_backward
