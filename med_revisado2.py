import os
import sys

import numpy as np
from decimal import Decimal, getcontext

path_quadratura = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(path_quadratura)

from quadratura.quadratura_backend import quadratura

getcontext().prec = 50


def med(
    sigmaT,
    sigmaS0,
    sigmaS1,
    sigmaS2,
    Qj,
    NiSigmaF,
    N,
    cce,
    ccd,
    precisao,
    NN,
    regioes,
    n_regioes,
    esp_R,
):
    N = int(N)  # Ordem da Quadratura
    n_regioes = int(n_regioes)  # Quantidade de regiões
    mi, w = quadratura(N)  # Mis e Omegas da quadratura
    pt = int(sum(NN) + 1)  # Número de pontos totais
    NNT = int(sum(NN))  # Número de nodos totais

    psiX = [[0 for _ in range(N)] for _ in range(pt)]  # Criando lista com psis iniciais
    for i in range(N // 2):
        psiX[0][i] = cce
        psiX[NNT][N // 2 + i] = ccd

    hj = [0 for _ in range(n_regioes)]
    for regiao in range(n_regioes):
        hj[regiao] = esp_R[regiao] / NN[regiao]  # Espessura do nodo

    C0j = []
    for i in range(len(sigmaT)):
        C0j.append(sigmaS0[i] / sigmaT[i])

    matriz_A = [[0 for _ in range(N)] for _ in range(N)]
    matriz_B = [[0 for _ in range(N)] for _ in range(N)]
    matrizes_eig = []
    matrizes_particular = []
    for regiao in regioes:
        for i in range(N):
            for j in range(N):
                if i == j:
                    matriz_A[i][j] = float(
                        (1 / mi[i]) - ((C0j[regiao - 1] * w[j]) / (2 * mi[i]))
                    )
                else:
                    matriz_A[i][j] = float(-((C0j[regiao - 1] * w[j]) / (2 * mi[i])))
        matrizes_eig.append(matriz_A)

        # Matriz para encontrar os fluxos da parte particular da solução
        for i in range(N):
            for j in range(N):
                if i == j:
                    matriz_B[i][j] = float(
                        sigmaT[regiao - 1] - ((sigmaS0[regiao - 1] * w[j]) / 2)
                    )
                else:
                    matriz_B[i][j] = float(-((sigmaS0[regiao - 1] * w[j]) / 2))

        # Encontrando matrizes inversas da solução particular
        matriz_inversa = np.linalg.inv(matriz_B)
        matrizes_particular.append(matriz_inversa)
        del matriz_inversa  # Para não dar erro, caso vc do futuro tenha uma solução melhor...

    # Encontrando autovalores e autovetores
    autovalores = []
    autovetores = []
    for matriz in matrizes_eig:
        autovalor_lambda, autovetor = np.linalg.eig(matriz)
        autovalores.append(autovalor_lambda.tolist())
        autovetores.append(autovetor.tolist())

    # Transformando Lambda em Ni
    for i, autovalor in enumerate(autovalores):
        for j, numero in enumerate(autovalor):
            autovalores[i][j] = 1 / numero

    # Encontrando soluções particulares
    fonte = [float(Qj[regiao - 1]) for _ in range(N)]
    solucoes_particulares = []
    for matriz in matrizes_particular:
        solucoes_particulares.append((matriz @ fonte).tolist())
