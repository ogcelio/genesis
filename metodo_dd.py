import os
import sys
from decimal import Decimal, getcontext

# DECIMAL UTILIZADO PARA QUE SEJAM EVITADOS ERROS DEVIDO A UTILIZAÇÃO DO
# TYPE FLOAT

import numpy as np

# Tornando a quadratura possível de ser importada
path_quadratura = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(path_quadratura)

from quadratura.quadratura_backend import quadratura


def diamond_difference(
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
    getcontext().prec = 50
    iteracao = 0  # Iniciando as iterações
    N = int(N)
    n_regioes = int(n_regioes)
    mi, w = quadratura(N)  # Mis e Omegas da quadratura
    pt = int(sum(NN) + 1)  # Número de pontos totais
    NNT = int(sum(NN))  # Número de nodos totais

    teste_0 = False
    for i in range(len(Qj)):
        if Qj[i] != 0.0:
            teste_0 = True  # Teste para saber se todas as fontes são 0
            break

    hj = [0 for _ in range(n_regioes)]
    for regiao in range(n_regioes):
        hj[regiao] = esp_R[regiao] / NN[regiao]  # Espessura do nodo

    ###ETAPA estimativas iniciais:
    psiX = [[0 for _ in range(N)] for _ in range(pt)]  # criando lista com psis iniciais
    for i in range(N // 2):
        psiX[0][i] = cce
        psiX[NNT][N // 2 + i] = ccd

    while True:
        iteracao += 1
        ###ETAPA CÁLCULO DOS PSIS MÉDIOS
        psiM = []
        for j in range(NNT):
            psiM_aux = []
            for m in range(N):
                psiM_aux.append(Decimal("0.5") * (psiX[j + 1][m] + psiX[j][m]))
            psiM.append(psiM_aux)

        ###ETAPA CÁLCULO DO Ssj
        regiao = regioes[0] - 1
        nodo = 0
        Ssj = []
        i = 0
        for j in range(NNT):
            soma = 0
            if nodo == NN[i]:
                i += 1
                regiao = regioes[i] - 1
                nodo = 0

            for m in range(N):
                soma += w[m] * psiM[j][m]
            Ssj.append((sigmaS0[regiao] / 2) * soma)
            nodo += 1

        ###ETAPA CÁLCULO DO FI INICIAL
        fi_inicial = []
        for x in range(pt):
            soma_fi = 0
            for m in range(N):
                soma_fi += w[m] * psiX[x][m]
            fi_inicial.append(Decimal("0.5") * soma_fi)

        if ccd == 0.0 and cce == 0.0 and teste_0 == False:
            # Arredondando fi_final
            fi_inicial_formatado = [float(fi) for fi in fi_inicial]

            # Arredondando psiX
            psiX_formatado = [[float(f"{fluxo}") for fluxo in linha] for linha in psiX]
            taxa_absorcao = [0 for _ in range(n_regioes)]
            taxa_fuga = [0, 0]
            return (
                fi_inicial_formatado,
                psiX_formatado,
                iteracao,
                taxa_absorcao,
                taxa_fuga,
            )  # Caso fontes e condições de contorno sejam nulas, o código retorna os fluxos completamente preenchidos de zeros

        ###ETAPA IDA
        regiao = regioes[0] - 1
        nodo = 0
        i = 0
        for j in range(1, pt):
            if nodo == NN[i]:
                i += 1
                regiao = regioes[i] - 1
                nodo = 0
            for m in range(N // 2):
                psiX[j][m] = (
                    (((mi[m] / hj[i]) - (sigmaT[regiao] / 2)) * psiX[j - 1][m])
                    + Ssj[j - 1]
                    + Qj[regiao]
                ) / ((mi[m] / hj[i]) + (sigmaT[regiao] / 2))
            nodo += 1

        ###ETAPA VOLTA
        ultima_regiao = len(regioes) - 1
        regiao = regioes[ultima_regiao] - 1
        nodo = 0
        i = ultima_regiao
        for j in range(NNT - 1, -1, -1):
            if nodo == NN[i]:
                i -= 1
                regiao = regioes[i] - 1
                nodo = 0
            for m in range((N // 2), N):
                psiX[j][m] = (
                    (((abs(mi[m]) / hj[i]) - (sigmaT[regiao] / 2)) * psiX[j + 1][m])
                    + Ssj[j]
                    + Qj[regiao]
                ) / ((abs(mi[m]) / hj[i]) + (sigmaT[regiao] / 2))
            nodo += 1

        ###ETAPA CÁLCULO DO FI FINAL
        fi_final = []
        for x in range(pt):
            soma_fi = 0
            for m in range(N):
                soma_fi += w[m] * psiX[x][m]
            fi_final.append(Decimal("0.5") * soma_fi)

        if iteracao > 1:
            ###ETAPA CÁLCULO DO DR

            # Transformando em arrays numpy para realizar a subtração
            fi_inicial = np.array(fi_inicial)
            fi_final = np.array(fi_final)

            resultado = abs(fi_inicial - fi_final)

            # Transformando em listas
            resultado = resultado.tolist()
            fi_inicial = fi_inicial.tolist()

            # Coletando os maiores de cada vetor, em módulo
            maior_inicial = max(fi_inicial, key=abs)
            maior_final = max(resultado, key=abs)

            dr = abs(maior_final / maior_inicial)
            if dr < precisao:
                break

    # Arredondando fi_final
    fi_final = fi_final.tolist()
    fi_final_formatado = [round(float(fi), 4) for fi in fi_final]

    # Arredondando psiX
    psiX_formatado = [[float(f"{fluxo:.4f}") for fluxo in linha] for linha in psiX]

    # TAXA DE ABSORÇÃO
    fi_medio = []
    sigmaA = []
    regiao = regioes[0] - 1
    soma = 0
    i = 0
    nodo = 0
    for j in range(NNT):
        if nodo == NN[i]:
            i += 1
            regiao = regioes[i] - 1
            nodo = 0
        for m in range(N):
            soma += w[m] * psiM[j][m]
        fi_medio.append(Decimal("0.5") * soma)
        soma = 0
        nodo += 1

    # Gerando Sigma A
    for regiao in regioes:
        sigmaA.append(sigmaT[regiao - 1] - sigmaS0[regiao - 1])

    taxa_absorcao = []
    soma = 0
    nodo = 1
    i = 0
    for j in range(NNT):
        soma += sigmaA[i] * fi_medio[j]
        if nodo == NN[i]:
            i += 1
            taxa_absorcao.append(soma)
            soma = 0
            nodo = 0
        nodo += 1

    # FUGA EM 0
    taxa_fuga = []
    soma = 0
    for m in range(N // 2, N):
        soma += abs(mi[m] * w[m] * psiX[0][m])
    taxa_fuga.append(soma)

    # FUGA NO MÁXIMO DA ÚLTIMA REGIÃO
    soma = 0
    for m in range(N // 2):
        soma += abs(mi[m] * w[m] * psiX[len(psiX) - 1][m])
    taxa_fuga.append(soma)

    return fi_final_formatado, psiX_formatado, iteracao, taxa_absorcao, taxa_fuga
